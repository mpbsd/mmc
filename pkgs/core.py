#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
from datetime import datetime

# RE {{{
RE = {
    "HPW": {
        "2": {
            "M": r"^[0-9]M[0-9]{1,3}$",
            "T": r"^[0-9]T[0-9]{1,3}$",
            "N": r"^[0-9]N[0-9]{1,3}$",
            "A": r"^[0-9][MTN][0-9]{1,3}$",
        },
        "4": {
            "M": r"^[0-9]{2}M[0-9]{2}$",
            "T": r"^[0-9]{2}T[0-9]{2}$",
            "N": r"^[0-9]{2}N[0-9]{2}$",
            "A": r"^[0-9]{2}[MTN][0-9]{2}$",
        },
        "6": {
            "M": r"^[0-9]{3}M[0-9]{2}$",
            "T": r"^[0-9]{3}T[0-9]{2}$",
            "N": r"^[0-9]{3}N[0-9]{2}$",
            "A": r"^[0-9]{3}[MTN][0-9]{2}$",
        },
    }
}
# }}}


def REGEXP(pattern, input):
    regexp = re.compile(pattern)
    return bool(regexp.match(input))


def COMPONENTS_TIMETABLE(timetable):
    RE_TIMETABLE = re.compile(r"^([0-9]+)([MTN])([0-9]+)$")
    return [x for x in RE_TIMETABLE.split(timetable) if x != ""]


def HPW(timetable):
    M = len(COMPONENTS_TIMETABLE(timetable)[0])
    N = len(COMPONENTS_TIMETABLE(timetable)[2])
    return M * N


def INDIVIDUAL_DIGITS(number):
    RE_DIGITS = re.compile(r"([1-6])")
    return [int(x) for x in RE_DIGITS.split(number) if x != ""]


def WEEKDAYS(timetable):
    COMP = COMPONENTS_TIMETABLE(timetable)
    return COMP[0]


def PERIOD_OF_THE_DAY(timetable):
    COMP = COMPONENTS_TIMETABLE(timetable)
    return COMP[1]


def ORDINALS(timetable):
    COMP = COMPONENTS_TIMETABLE(timetable)
    return COMP[2]


def CURRENT_SEMESTER():
    y = datetime.today().strftime("%Y")
    m = datetime.today().strftime("%m")
    return f"{y}_1" if int(m) < 7 else f"{y}_2"


def CLASSES_TAKE_PLACE_IN_THE_SAME_CAMPUS(blobslist):
    return True if len([blob[0] for blob in blobslist]) == 1 else False


def CLASSES_ARE_CONSECUTIVE(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    DIGT1 = DIGITS(COMP1[2])
    DIGT2 = DIGITS(COMP2[2])
    COND0 = len([x for x in DIGITS(COMP1[0]) if x in DIGITS(COMP2[0])]) > 0
    COND1 = COMP1[1] == COMP2[1]
    COND2 = (DIGT1[1] + 1 == DIGT2[0]) or (DIGT2[1] + 1 == DIGT1[0])
    return COND0 and COND1 and COND2


def CLASSES_OCCUR_IN_THE_SAME_DAYS(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    return COMP1[0] == COMP2[0]


def CLASSES_OCCUR_IN_THE_SAME_PERIOD(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    return COMP1[1] == COMP2[1]


def main():
    SEMESTER = CURRENT_SEMESTER()

    with sqlite3.connect("data/sql/sqlite.db") as connection:
        connection.create_function("REGEXP", 2, REGEXP)
        cursor = connection.cursor()

        HPW08 = cursor.execute(
            "SELECT * FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " B1.aterm = ?"
            " AND"
            " B1.aterm = B2.aterm"
            " AND"
            " B1.place = B2.place"
            " AND"
            " B1.setup REGEXP ?"
            " AND"
            " B2.setup REGEXP ?",
            [SEMESTER, RE["HPW"]["4"]["A"], RE["HPW"]["4"]["A"]]
        ).fetchall()

        HPW10 = cursor.execute(
            "SELECT * FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " B1.aterm = ?"
            " AND"
            " B1.aterm = B2.aterm"
            " AND"
            " B1.place = B2.place"
            " AND"
            " B1.setup REGEXP ?"
            " AND"
            " B2.setup REGEXP ?",
            [SEMESTER, RE["HPW"]["4"]["A"], RE["HPW"]["6"]["A"]]
        ).fetchall()

        HPW12_P1 = cursor.execute(
            "SELECT * FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " B1.aterm = ?"
            " AND"
            " B1.aterm = B2.aterm"
            " AND"
            " B1.place = B2.place"
            " AND"
            " B1.setup REGEXP ?"
            " AND"
            " B2.setup REGEXP ?",
            [SEMESTER, RE["HPW"]["6"]["A"], RE["HPW"]["6"]["A"]]
        ).fetchall()

        HPW12_P2 = cursor.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  C1.place2 AS place2,"
            "  C1.gradc2 AS gradc2,"
            "  C1.field2 AS field2,"
            "  C1.setup2 AS setup2,"
            "  C1.aterm2 AS aterm2,"
            "  C1.place3 AS place3,"
            "  C1.gradc3 AS gradc3,"
            "  C1.field3 AS field3,"
            "  C1.setup3 AS setup3,"
            "  C1.aterm3 AS aterm3 "
            "FROM blob AS B1 CROSS JOIN("
            "  SELECT "
            "    B2.place AS place2,"
            "    B2.gradc AS gradc2,"
            "    B2.field AS field2,"
            "    B2.setup AS setup2,"
            "    B2.aterm AS aterm2,"
            "    B3.place AS place3,"
            "    B3.gradc AS gradc3,"
            "    B3.field AS field3,"
            "    B3.setup AS setup3,"
            "    B3.aterm AS aterm3"
            "  FROM blob AS B2 CROSS JOIN blob AS B3"
            "  WHERE"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3) AS C1 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup2 REGEXP ?"
            "  AND"
            "  setup3 REGEXP ?",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"]
            ]
        ).fetchall()

        HPW12 = HPW12_P1 + HPW12_P2

        HPW14 = cursor.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  C1.place2 AS place2,"
            "  C1.gradc2 AS gradc2,"
            "  C1.field2 AS field2,"
            "  C1.setup2 AS setup2,"
            "  C1.aterm2 AS aterm2,"
            "  C1.place3 AS place3,"
            "  C1.gradc3 AS gradc3,"
            "  C1.field3 AS field3,"
            "  C1.setup3 AS setup3,"
            "  C1.aterm3 AS aterm3 "
            "FROM blob AS B1 CROSS JOIN("
            "  SELECT "
            "    B2.place AS place2,"
            "    B2.gradc AS gradc2,"
            "    B2.field AS field2,"
            "    B2.setup AS setup2,"
            "    B2.aterm AS aterm2,"
            "    B3.place AS place3,"
            "    B3.gradc AS gradc3,"
            "    B3.field AS field3,"
            "    B3.setup AS setup3,"
            "    B3.aterm AS aterm3"
            "  FROM blob AS B2 CROSS JOIN blob AS B3"
            "  WHERE"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3) AS C1 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup2 REGEXP ?"
            "  AND"
            "  setup3 REGEXP ?",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"],
                RE["HPW"]["6"]["A"]
            ]
        ).fetchall()

        HPW16_P1 = cursor.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  C1.place2 AS place2,"
            "  C1.gradc2 AS gradc2,"
            "  C1.field2 AS field2,"
            "  C1.setup2 AS setup2,"
            "  C1.aterm2 AS aterm2,"
            "  C1.place3 AS place3,"
            "  C1.gradc3 AS gradc3,"
            "  C1.field3 AS field3,"
            "  C1.setup3 AS setup3,"
            "  C1.aterm3 AS aterm3 "
            "FROM blob AS B1 CROSS JOIN("
            "  SELECT "
            "    B2.place AS place2,"
            "    B2.gradc AS gradc2,"
            "    B2.field AS field2,"
            "    B2.setup AS setup2,"
            "    B2.aterm AS aterm2,"
            "    B3.place AS place3,"
            "    B3.gradc AS gradc3,"
            "    B3.field AS field3,"
            "    B3.setup AS setup3,"
            "    B3.aterm AS aterm3"
            "  FROM blob AS B2 CROSS JOIN blob AS B3"
            "  WHERE"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3) AS C1 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup2 REGEXP ?"
            "  AND"
            "  setup3 REGEXP ?",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["6"]["A"],
                RE["HPW"]["6"]["A"]
            ]
        )

        HPW16_P2 = cursor.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  C1.place2 AS place2,"
            "  C1.gradc2 AS gradc2,"
            "  C1.field2 AS field2,"
            "  C1.setup2 AS setup2,"
            "  C1.aterm2 AS aterm2,"
            "  C1.place3 AS place3,"
            "  C1.gradc3 AS gradc3,"
            "  C1.field3 AS field3,"
            "  C1.setup3 AS setup3,"
            "  C1.aterm3 AS aterm3 "
            "FROM blob AS B1 CROSS JOIN("
            "  SELECT "
            "    B2.place AS place2,"
            "    B2.gradc AS gradc2,"
            "    B2.field AS field2,"
            "    B2.setup AS setup2,"
            "    B2.aterm AS aterm2,"
            "    B3.place AS place3,"
            "    B3.gradc AS gradc3,"
            "    B3.field AS field3,"
            "    B3.setup AS setup3,"
            "    B3.aterm AS aterm3"
            "  FROM blob AS B2 CROSS JOIN blob AS B3"
            "  WHERE"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3) AS C1 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup2 REGEXP ?"
            "  AND"
            "  setup3 REGEXP ?",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["6"]["A"],
                RE["HPW"]["6"]["A"]
            ]
        ).fetchall()

        HPW16 = HPW16_P1 + HPW16_P2

        print(HPW16)


if __name__ == "__main__":
    main()
