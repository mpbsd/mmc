import re
import sqlite3
import sys
import tomllib
from itertools import combinations
from pathlib import Path

from pkgs.blob import BLOB, NAME, PKEY, REGEXP, Conn


def DIGITS(number: str) -> list[int] | None:
    RE = re.compile(r"^[0-9]+$")
    if RE.match(number):
        LN = sorted([int(x) for x in number])
    else:
        LN = None
    return LN


def TIMETABLE_COMPONENTS(conn: Conn, pkey: str) -> tuple | None:
    RE = re.compile(r"^([2-6]{1,3})([mtn])([1-6]{1,3})$", re.I)
    TT = NAME(conn, "horario", pkey)
    C0 = None
    if TT:
        C1 = RE.match(TT)
        if C1:
            C0 = (DIGITS(C1.group(1)), C1.group(2), DIGITS(C1.group(3)))
    return C0


def HOURS_PER_WEEK(connection: Conn, pkey_tt: str) -> int | None:
    C = TIMETABLE_COMPONENTS(connection, pkey_tt)
    if C:
        H = len(C[0]) * len(C[2])
    else:
        H = None
    return H


def OVERLAPPING_CLASSES(connection: Conn, blob: tuple) -> bool:
    N = len(blob) // 5
    T = [TIMETABLE_COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
    B = 1
    for t1, t2 in combinations(T, 2):
        C0 = len([d for d in t1[0] if d in t2[0]]) > 0
        C1 = t1[1] == t2[1]
        C2 = len([h for h in t1[2] if h in t2[2]]) > 0
        if C0 and C1 and C2:
            B *= 0
    return True if (B == 0) else False


def REPEATING_DISCIPLINES(blob):
    N = len(blob) // 5
    L = len(set([blob[i * 5 + 2] for i in range(N)]))
    return True if (L < N) else False


def RECURRING_DAYS(connection, blob):
    N = len(blob) // 5
    T = [TIMETABLE_COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
    B = 1
    for t1, t2 in combinations(T, 2):
        if (t1[0] <= t2[0] or t2[0] <= t1[0]) is False:
            B *= 0
    return True if (B == 1) else False


def CONTIGUOUS_CLASSES(connection, blob):
    N = len(blob) // 5
    T = [TIMETABLE_COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
    B = 1
    for t1, t2 in combinations(T, 2):
        C0 = len([d for d in t1[0] if d in t2[0]]) > 0
        C1 = t1[1] == t2[1]
        C2 = (t1[2][-1] == t2[2][0] - 1) or (t2[2][-1] == t1[2][0] - 1)
        if (C0 and C1 and C2) is False:
            B *= 0
    return True if (B == 1) else False


def SCORE(score, table, field):
    S = 0
    if (table in score.keys()) and (field in score[table].keys()):
        S = score[table][field]
    return S


# TODO: add extra points for configurations in a single campus, if the campus is
# either colemar (1) or samambaia (2)
def RANK(connection, score, blob):
    N = len(blob) // 5
    S = 0
    for i in range(N):
        S += SCORE(score, "campus", blob[i * 5])
        S += SCORE(score, "curso", blob[i * 5 + 1])
        S += SCORE(score, "disciplina", blob[i * 5 + 2])
        S += SCORE(score, "horario", blob[i * 5 + 3])
    S += 1 if REPEATING_DISCIPLINES(blob) else 0
    S += 1 if RECURRING_DAYS(connection, blob) else 0
    S += 1 if CONTIGUOUS_CLASSES(connection, blob) else 0
    return S / N


def DECODE(connection, blob):
    N = len(blob) // 5
    X = []
    for i in range(N):
        campus = NAME(connection, "campus", blob[i * 5])
        curso = NAME(connection, "curso", blob[i * 5 + 1])
        disciplina = NAME(connection, "disciplina", blob[i * 5 + 2])
        horario = NAME(connection, "horario", blob[i * 5 + 3])
        semestre = NAME(connection, "semestre", blob[i * 5 + 4])
        X.append((campus, curso, disciplina, horario, semestre))
    return X


def CAMPUSES_FROM_ALL_CONFIGURATIONS(blob):
    return set([[x[0] for x in X] for X in blob])


def DISCIPLINES_FROM_ALL_BLOBS(blob):
    N = len(blob) // 5
    return set([blob[i * 5 + 2] for i in range(N)])


def DAY_PERIOD_FROM_ALL_CONFIGURATIONS(connection, blob):
    N = len(blob) // 5
    return set([TIMETABLE_COMPONENTS(connection, blob[i * 5 + 3])[1] for i in range(N)])


def NON_REPEATING_DISCIPLINES(blob):
    N = len(blob) // 5
    M = len(set([blob[i * 5 : i * 5 + 5] for i in range(N)]))
    return M == N


def NOCTURNE_CLASSES(connection, blob):
    X = DAY_PERIOD_FROM_ALL_CONFIGURATIONS(connection, blob)
    return "n" in X


def NOT_ONLY_IN_THE_SAME_PERIOD_OF_THE_DAY(connection, blob):
    return len(DAY_PERIOD_FROM_ALL_CONFIGURATIONS(connection, blob)) >= 2


def AT_LEAST_SOME_CLASS_AT_FCT(blob):
    return 3 in CAMPUSES_FROM_ALL_CONFIGURATIONS(blob)


def HEALTH_OF_THE_BLOBS_COLLECTION(connection, blob):
    X = NON_REPEATING_DISCIPLINES(blob)
    Y = NOCTURNE_CLASSES(connection, blob)
    Z = NOT_ONLY_IN_THE_SAME_PERIOD_OF_THE_DAY(connection, blob)
    W = AT_LEAST_SOME_CLASS_AT_FCT(blob)
    return X and Y and Z and W


def FIRST_EIGHT_VALID_CONFIGURATIONS(connection, BLOB):
    X = [BLOB[0]]
    i = 1
    j = 1
    while i < 8:
        x = DISCIPLINES_FROM_ALL_BLOBS(X)
        NON_REPEATED_DISCIPLINE = True
        N = len(BLOB[j]) // 5
        for y in [BLOB[j][i * 5 : i * 5 + 5] for i in range(N)]:
            if y in x:
                NON_REPEATED_DISCIPLINE = False
                j += 1
        if NON_REPEATED_DISCIPLINE is True:
            X.append(BLOB[j])
            i += 1
            j += 1
    return X


def main():

    data = "data/sqlite.db"
    conf = "pkgs/conf.toml"

    if Path(data).is_file() is False:
        sys.exit(10)

    if Path(conf).is_file() is False:
        sys.exit(11)

    if len(sys.argv) != 3:
        sys.exit(12)

    if sys.argv[1] not in ["-p", "--profile"]:
        sys.exit(13)

    if sys.argv[2] not in ["8", "10", "12", "14", "16"]:
        sys.exit(14)

    with sqlite3.connect(data) as connection:
        connection.create_function("REGEXP", 2, REGEXP)

        score = {}

        with open(conf, "rb") as raw_toml_file:
            toml_file = tomllib.load(raw_toml_file)
            for table in toml_file.keys():
                score[table] = {}
                for field in toml_file[table].keys():
                    pkey = PKEY(connection, table, field)
                    score[table][pkey] = toml_file[table][field]

        blob = sorted(
            [
                B
                for B in BLOB(connection, int(sys.argv[2]))
                if OVERLAPPING_CLASSES(connection, B) is False
            ],
            key=lambda B: RANK(connection, score, B),
            reverse=True,
        )

        with open("sorted.txt", "w") as sorted_results:
            for b in blob:
                print(
                    DECODE(connection, b),
                    file=sorted_results,
                )


if __name__ == "__main__":
    main()
