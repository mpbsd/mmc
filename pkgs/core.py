#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
from datetime import datetime


def REGEXP(pattern, input):
    regexp = re.compile(pattern)
    return bool(regexp.match(input))


def SEMESTER():
    A = datetime.today().strftime("%Y")
    M = datetime.today().strftime("%m")
    return f"{A}_1" if int(M) < 7 else f"{A}_2"


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


def FETCH_TIMETABLE_COMPONENTS(connection, pkey_timetable):
    re_timetable = re.compile(r"^([0-9]{1,3})([mtn])([0-9]{1,3})$", re.I)
    timetable = NAME(connection, "horario", pkey_timetable)
    components = None
    if (timetable is not None) and (re_timetable.match(timetable) is not None):
        components = re_timetable.match(timetable).groups()
    return components


def HOURS_PER_WEEK(connection, pkey_timetable):
    C = FETCH_TIMETABLE_COMPONENTS(connection, pkey_timetable)
    M = len(C[0])
    N = len(C[2])
    return M * N


def DIGITS(number):
    re_digits = re.compile(r"^[0-9]+$")
    digits = None
    if re_digits.match(number):
        digits = [x for x in number]
    return digits


def BLOB(connection, profile):
    semester = PKEY(connection, "semestre", SEMESTER())
    RE = {
        # 4HPW {{{
        "4HPW": r"^[0-9]{2}[mtn][0-9]{2}$",
        # }}}
        # 6HPW {{{
        "6HPW": r"^[0-9]{3}[mtn][0-9]{2}$",
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
            ") LIMIT 1024;"
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
            ") LIMIT 1024;"
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
            ") LIMIT 1024;"
        ),
        # }}}
    }
    if profile == 8:
        # 08HPW {{{
        blob = connection.execute(
            QUERY["2BLOBS"], [semester, RE["4HPW"], RE["4HPW"]]
        ).fetchall()
        # }}}
    elif profile == 10:
        # 10HPW {{{
        blob = connection.execute(
            QUERY["2BLOBS"], [semester, RE["4HPW"], RE["6HPW"]]
        ).fetchall()
        # }}}
    elif profile == 12:
        # 12HPW {{{
        blob_1 = connection.execute(
            QUERY["3BLOBS"],
            [semester, RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = connection.execute(
            QUERY["2BLOBS"], [semester, RE["6HPW"], RE["6HPW"]]
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    elif profile == 14:
        # 14HPW {{{
        blob = connection.execute(
            QUERY["3BLOBS"],
            [semester, RE["4HPW"], RE["4HPW"], RE["6HPW"]],
        ).fetchall()
        # }}}
    elif profile == 16:
        # 16HPW {{{
        blob_1 = connection.execute(
            QUERY["4BLOBS"],
            [semester, RE["4HPW"], RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = connection.execute(
            QUERY["3BLOBS"],
            [semester, RE["4HPW"], RE["6HPW"], RE["6HPW"]],
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    else:
        blob = None
    return blob


def main():
    with sqlite3.connect("data/sql/sqlite.db") as connection:
        connection.create_function("REGEXP", 2, REGEXP)
        print(BLOB(connection, 8))


if __name__ == "__main__":
    main()
