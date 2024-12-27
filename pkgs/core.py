import re
import sqlite3
import sys
import tomllib
from functools import reduce
from itertools import combinations
from pathlib import Path

from pkgs.blob import BLOB, NAME, PKEY, REGEXP, Blob, Conn

F = {
    "campus": 0,
    "curso": 1,
    "disciplina": 2,
    "horario": 3,
    "semestre": 4,
}
f = len(F.keys())


def DIGITS(number: str) -> list[int] | None:
    RE = re.compile(r"^[0-9]+$")
    if RE.match(number):
        LN = sorted([int(x) for x in number])
    else:
        LN = None
    return LN


def TIMETABLE_COMPONENTS(conn: Conn, pkey: int) -> tuple | None:
    RE = re.compile(r"^([2-6]{1,3})([mtn])([1-6]{1,3})$", re.I)
    TT = NAME(conn, "horario", pkey)
    C0 = None
    if TT:
        C1 = RE.match(TT)
        if C1:
            C0 = (DIGITS(C1.group(1)), C1.group(2), DIGITS(C1.group(3)))
    return C0


def HOURS_PER_WEEK(conn: Conn, pkey: int) -> int | None:
    C = TIMETABLE_COMPONENTS(conn, pkey)
    if C:
        H = len(C[0]) * len(C[2])
    else:
        H = None
    return H


def OVERLAPPING_CLASSES(conn: Conn, blob: Blob) -> bool:
    N = len(blob) // f
    B = 1
    for i, j in combinations(range(N), 2):
        TI = TIMETABLE_COMPONENTS(conn, blob[i * f + F["horario"]])
        TJ = TIMETABLE_COMPONENTS(conn, blob[j * f + F["horario"]])
        if TI and TJ:
            C0 = len([d for d in TI[0] if d in TJ[0]]) > 0
            C1 = TI[1] == TJ[1]
            C2 = len([h for h in TI[2] if h in TJ[2]]) > 0
            if C0 and C1 and C2:
                B *= 0
    return True if (B == 0) else False


def REPEATING_DISCIPLINES(blob: Blob) -> bool:
    N = len(blob) // f
    L = len(set([blob[i * f + F["disciplina"]] for i in range(N)]))
    return True if (L < N) else False


def RECURRING_DAYS(conn: Conn, blob: Blob) -> bool:
    N = len(blob) // f
    B = 1
    for i, j in combinations(range(N), 2):
        TI = TIMETABLE_COMPONENTS(conn, blob[i * f + F["horario"]])
        TJ = TIMETABLE_COMPONENTS(conn, blob[j * f + F["horario"]])
        if TI and TJ:
            CI = [d for d in TI[0] if d in TJ[0]]
            CJ = [d for d in TJ[0] if d in TI[0]]
            if (CI == TI or CJ == TJ) is False:
                B *= 0
    return True if (B == 1) else False


def CONTIGUOUS_CLASSES(conn: Conn, blob: Blob) -> bool:
    N = len(blob) // f
    B = 1
    for i, j in combinations(range(N), 2):
        TI = TIMETABLE_COMPONENTS(conn, blob[i * f + F["horario"]])
        TJ = TIMETABLE_COMPONENTS(conn, blob[j * f + F["horario"]])
        if TI and TJ:
            C0 = len([d for d in TI[0] if d in TJ[0]]) > 0
            C1 = TI[1] == TJ[1]
            C2 = (TI[2][-1] == TJ[2][0] - 1) or (TJ[2][-1] == TI[2][0] - 1)
            if (C0 and C1 and C2) is False:
                B *= 0
    return True if (B == 1) else False


def SCORE(score: dict, tbl: str, key: int) -> int:
    S = 0
    if (tbl in score.keys()) and (key in score[tbl].keys()):
        S = score[tbl][key]
    return S


def CAMPUSES(blob: Blob) -> list[int]:
    N = len(blob) // f
    C = []
    for i in range(N):
        C.append(blob[i * f + F["campus"]])
    return C


def RANK(conn: Conn, score, blob: Blob) -> float:
    C = CAMPUSES(blob)
    N = len(blob) // f
    S = 0
    for i in range(N):
        S += SCORE(score, "campus", blob[i * f + F["campus"]])
        S += SCORE(score, "curso", blob[i * f + F["curso"]])
        S += SCORE(score, "disciplina", blob[i * f + F["disciplina"]])
        S += SCORE(score, "horario", blob[i * f + F["horario"]])
    S += 1 if (len(set(C)) == 1) else 0
    S += 1 if (3 not in C) else -1
    S += 1 if REPEATING_DISCIPLINES(blob) else 0
    S += 1 if RECURRING_DAYS(conn, blob) else 0
    S += 1 if CONTIGUOUS_CLASSES(conn, blob) else 0
    return S / N


def DECODE(conn: Conn, blob: Blob) -> list[tuple[str]]:
    N = len(blob) // f
    X = []
    for i in range(N):
        campus = NAME(conn, "campus", blob[i * f + F["campus"]])
        curso = NAME(conn, "curso", blob[i * f + F["curso"]])
        disciplina = NAME(conn, "disciplina", blob[i * f + F["disciplina"]])
        horario = NAME(conn, "horario", blob[i * f + F["horario"]])
        semestre = NAME(conn, "semestre", blob[i * f + F["semestre"]])
        X.append((campus, curso, disciplina, horario, semestre))
    return X


def DISCIPLINES(blob: Blob) -> list[Blob]:
    N = len(blob) // f
    D = []
    for i in range(N):
        D.append(blob[i * f + F["curso"] : i * f + F["horario"] + 1])
    return D


def HEALTH(x: int, C: list[str], D: list[int]) -> list[int]:
    C1 = 1 if (x == 1) else 0
    C2 = 1 if ((len(C) >= 2) and ("n" in C)) else 0
    C3 = 1 if (3 in D) else 0
    return [C1, C2, C3]


# There are four lists, named A, B, C and D
#
#  A: for the blobs themselves
#  B: for the disciplines
#  C: for the periods of the day
#  D: for the campuses
#
# TODO: add upper bounds to prevent overflows
def EIGHT_FIRST_VALID_ONES(conn: Conn, BLOB: list[Blob]) -> list[Blob]:
    A = [BLOB[0]]
    B = DISCIPLINES(BLOB[0])
    x = 0
    i = 1
    while len(A) < 7:
        x = 0
        while x == 0:
            X = list(map(lambda y: 1 if y not in B else 0, DISCIPLINES(BLOB[i])))
            x = reduce(lambda r, s: r * s, X)
            i += 1
        A.append(BLOB[i])
        for y in DISCIPLINES(BLOB[i]):
            B.append(y)
        i += 1
    C = []
    D = []
    for j in range(7):
        N = len(A[j]) // f
        for k in range(N):
            T = TIMETABLE_COMPONENTS(conn, A[j][k * f + F["horario"]])
            if T:
                if T[1] not in C:
                    C.append(T[1])
            if A[j][k * f + F["campus"]] not in D:
                D.append(A[j][k * f + F["campus"]])
    # _, C2, C3 = HEALTH(x, C, D)
    # if (C2 == 1) and (C3 == 0):
    # elif (C2 == 0) and (C3 == 1):
    # elif (C2 == 1) and (C3 == 1):
    # TODO: be smart and go first for the things that matter most ;)
    return A


def main():

    data = "data/sqlite.db"
    conf = "pkgs/conf.toml"

    if Path(data).is_file() is False:
        sys.exit(100)

    if Path(conf).is_file() is False:
        sys.exit(101)

    if len(sys.argv) != 3:
        sys.exit(102)

    if sys.argv[1] not in ["-p", "--profile"]:
        sys.exit(103)

    if sys.argv[2] not in ["8", "10", "12", "14", "16"]:
        sys.exit(104)

    with sqlite3.connect(data) as conn:
        conn.create_function("REGEXP", 2, REGEXP)

        score = {}

        with open(conf, "rb") as raw_toml_file:
            toml_file = tomllib.load(raw_toml_file)
            for table in toml_file.keys():
                score[table] = {}
                for field in toml_file[table].keys():
                    pkey = PKEY(conn, table, field)
                    score[table][pkey] = toml_file[table][field]

        B0 = BLOB(conn, int(sys.argv[2]))

        if B0:
            S = EIGHT_FIRST_VALID_ONES(conn, B0)

            print(S)
            # B1 = sorted(
            #     [B for B in B0 if OVERLAPPING_CLASSES(conn, B) is False],
            #     key=lambda B: RANK(conn, score, B),
            #     reverse=True,
            # )
            # with open("sorted.txt", "w") as sorted_results:
            #     for b in B1:
            #         print(
            #             DECODE(conn, b),
            #             file=sorted_results,
            #         )


if __name__ == "__main__":
    main()
