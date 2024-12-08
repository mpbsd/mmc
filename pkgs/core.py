#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
import sys
import tomllib
from datetime import datetime
from itertools import combinations
from pathlib import Path


def SEMESTER():
    Y = datetime.today().strftime("%Y")
    M = datetime.today().strftime("%m")
    return f"{Y}_1" if int(M) < 7 else f"{Y}_2"


def REGEXP(pattern, input):
    regexp = re.compile(pattern)
    return bool(regexp.match(input))


def BLOB(connection, profile):
    pkey_semester = PKEY(connection, "semestre", SEMESTER())
    RE = {
        # 4HPW {{{
        "4HPW": r"^[2-6]{2}[mtn][1-6]{2}$",
        # }}}
        # 6HPW {{{
        "6HPW": r"^[2-6]{3}[mtn][1-6]{2}$",
        # }}}
    }
    QUERY = {
        # 2BLOBS {{{
        "2BLOBS": (
            "SELECT"
            "  B1.campus,"
            "  B1.curso,"
            "  B1.disciplina,"
            "  B1.horario,"
            "  B1.semestre,"
            "  B2.campus,"
            "  B2.curso,"
            "  B2.disciplina,"
            "  B2.horario,"
            "  B2.semestre "
            "FROM"
            "  blob AS B1 "
            "JOIN"
            "  blob AS B2 "
            "ON"
            "  B1.semestre = B2.semestre "
            "WHERE ("
            "  B1.semestre = ? "
            "  AND"
            "  B1.horario != B2.horario"
            "  AND"
            "  EXISTS ("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B1.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS ("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B2.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  ) "
            ") LIMIT 4096;"
        ),
        # }}}
        # 3BLOBS {{{
        "3BLOBS": (
            "SELECT"
            "  B1.campus,"
            "  B1.curso,"
            "  B1.disciplina,"
            "  B1.horario,"
            "  B1.semestre,"
            "  B2.campus,"
            "  B2.curso,"
            "  B2.disciplina,"
            "  B2.horario,"
            "  B2.semestre,"
            "  B3.campus,"
            "  B3.curso,"
            "  B3.disciplina,"
            "  B3.horario,"
            "  B3.semestre "
            "FROM"
            "  blob AS B1 "
            "INNER JOIN"
            "  blob AS B2 "
            "ON"
            "  B1.semestre = B2.semestre "
            "INNER JOIN"
            "  blob AS B3 "
            "ON"
            "  B2.semestre = B3.semestre "
            "WHERE ("
            "  B1.semestre = ?"
            "  AND"
            "  B1.horario != B2.horario"
            "  AND"
            "  B1.horario != B3.horario"
            "  AND"
            "  B2.horario != B3.horario"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B1.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B2.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B3.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  ) "
            ") LIMIT 4096;"
        ),
        # }}}
        # 4BLOBS {{{
        "4BLOBS": (
            "SELECT"
            "  B1.campus,"
            "  B1.curso,"
            "  B1.disciplina,"
            "  B1.horario,"
            "  B1.semestre,"
            "  B2.campus,"
            "  B2.curso,"
            "  B2.disciplina,"
            "  B2.horario,"
            "  B2.semestre,"
            "  B3.campus,"
            "  B3.curso,"
            "  B3.disciplina,"
            "  B3.horario,"
            "  B3.semestre,"
            "  B4.campus,"
            "  B4.curso,"
            "  B4.disciplina,"
            "  B4.horario,"
            "  B4.semestre "
            "FROM"
            "  blob AS B1 "
            "INNER JOIN"
            "  blob AS B2 "
            "ON"
            "  B1.semestre = B2.semestre "
            "INNER JOIN"
            "  blob AS B3 "
            "ON"
            "  B2.semestre = B3.semestre "
            "INNER JOIN"
            "  blob AS B4 "
            "ON"
            "  B3.semestre = B4.semestre "
            "WHERE ("
            "  B1.semestre = ?"
            "  AND"
            "  B1.horario != B2.horario"
            "  AND"
            "  B1.horario != B3.horario"
            "  AND"
            "  B1.horario != B4.horario"
            "  AND"
            "  B2.horario != B3.horario"
            "  AND"
            "  B2.horario != B4.horario"
            "  AND"
            "  B3.horario != B4.horario"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B1.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B2.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B3.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS("
            "    SELECT"
            "      h.x"
            "    FROM"
            "      horario AS h"
            "    WHERE"
            "      h.x = B4.horario"
            "      AND"
            "      h.y REGEXP ?"
            "  ) "
            ") LIMIT 4096;"
        ),
        # }}}
    }
    if profile == 8:
        # 08HPW {{{
        blob = connection.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["4HPW"], RE["4HPW"]]
        ).fetchall()
        # }}}
    elif profile == 10:
        # 10HPW {{{
        blob = connection.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["4HPW"], RE["6HPW"]]
        ).fetchall()
        # }}}
    elif profile == 12:
        # 12HPW {{{
        blob_1 = connection.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = connection.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["6HPW"], RE["6HPW"]]
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    elif profile == 14:
        # 14HPW {{{
        blob = connection.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["6HPW"]],
        ).fetchall()
        # }}}
    elif profile == 16:
        # 16HPW {{{
        blob_1 = connection.execute(
            QUERY["4BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = connection.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["6HPW"], RE["6HPW"]],
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    else:
        blob = None
    return blob


def PKEY(connection, table, name):
    pkey = None
    if table in ["campus", "curso", "disciplina", "horario", "semestre"]:
        query = f"SELECT x FROM '{table}' WHERE y = '{name}'"
        response = connection.execute(query).fetchone()
        if response is not None:
            pkey = response[0]
    return pkey


def NAME(connection, table, pkey):
    name = None
    if table in ["campus", "curso", "disciplina", "horario", "semestre"]:
        query = f"SELECT y FROM '{table}' WHERE x = '{pkey}'"
        response = connection.execute(query).fetchone()
        if response is not None:
            name = response[0]
    return name


def DIGITS(number):
    re_digits = re.compile(r"^[0-9]+$")
    digits = None
    if re_digits.match(number):
        digits = [int(x) for x in number]
    return digits


def COMPONENTS(connection, pkey_timetable):
    re_timetable = re.compile(r"^([2-6]{1,3})([mtn])([1-6]{1,3})$", re.I)
    timetable = NAME(connection, "horario", pkey_timetable)
    components = None
    if (timetable is not None) and (re_timetable.match(timetable) is not None):
        CMP = re_timetable.match(timetable).groups()
        components = (sorted(DIGITS(CMP[0])), CMP[1], sorted(DIGITS(CMP[2])))
    return components


def HOURS_PER_WEEK(connection, pkey_timetable):
    C = COMPONENTS(connection, pkey_timetable)
    return len(C[0]) * len(C[1])


def OVERLAPPING_CLASSES(connection, blob):
    N = len(blob) // 5
    T = [COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
    B = 1
    for t1, t2 in combinations(T, 2):
        C0 = len([d for d in t1[0] if d in t2[0]]) > 0
        C1 = t1[1] == t2[1]
        C2 = len([h for h in t1[2] if h in t2[2]]) > 0
        if C0 and C1 and C2:
            B *= 0
    return True if (B == 0) else False


def SAME_CAMPUS(blob):
    N = len(blob) // 5
    L = len(set([blob[i * 5] for i in range(N)]))
    return True if (L == 1) else False


def REPEATING_DISCIPLINES(blob):
    N = len(blob) // 5
    L = len(set([blob[i * 5 + 2] for i in range(N)]))
    return True if (L < N) else False


def RECURRING_DAYS(connection, blob):
    N = len(blob) // 5
    T = [COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
    B = 1
    for t1, t2 in combinations(T, 2):
        if (t1[0] <= t2[0] or t2[0] <= t1[0]) is False:
            B *= 0
    return True if (B == 1) else False


def CONTIGUOUS_CLASSES(connection, blob):
    N = len(blob) // 5
    T = [COMPONENTS(connection, blob[i * 5 + 3]) for i in range(N)]
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


def RANK(connection, score, blob):
    N = len(blob) // 5
    S = 0
    for i in range(N):
        S += SCORE(score, "campus", blob[i * 5])
        S += SCORE(score, "curso", blob[i * 5 + 1])
        S += SCORE(score, "disciplina", blob[i * 5 + 2])
        S += SCORE(score, "horario", blob[i * 5 + 3])
    S += 2 if SAME_CAMPUS(blob) else 0
    S += 2 if REPEATING_DISCIPLINES(blob) else 0
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


def main():

    data = "data/sql/sqlite.db"
    conf = "pkgs/conf.toml"

    if Path(data).is_file() is False:
        sys.exit(10)
        sys.stderr(f"Database file not found: {data}")

    if Path(conf).is_file() is False:
        sys.exit(11)
        sys.stderr(f"Config file not found: {conf}")

    if len(sys.argv) != 3:
        sys.exit(12)
        sys.stderr("Incorrect function call: number of arguments must be 3")

    if sys.argv[1] not in ["-p", "--profile"]:
        sys.exit(13)
        sys.stderr("First flag must be either '-p' or '--profile'")

    if sys.argv[2] not in ["8", "10", "12", "14", "16"]:
        sys.exit(14)
        sys.stderr("Second flag must be either '8', '10', '12', '14' or '16'")

    with sqlite3.connect(data) as connection:
        connection.create_function("REGEXP", 2, REGEXP)

        score = {}

        with open(conf, "rb") as raw_toml_file:
            toml_file = tomllib.load(raw_toml_file)
            for table in toml_file.keys():
                score[table] = {}
                for field in toml_file[table].keys():
                    pkey = PKEY(connection, table, field)
                    priority = toml_file[table][field]["score"]
                    score[table][pkey] = priority

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
                print(DECODE(connection, b), file=sorted_results)


if __name__ == "__main__":
    main()
