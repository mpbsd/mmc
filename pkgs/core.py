#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
from datetime import datetime

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


def CHOICES(CURSOR, SEMESTER, HPW):
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
    if HPW == 8:
        # HPW08 {{{
        choices = CURSOR.execute(
            "SELECT"
            " B1.place AS place1,"
            " B1.gradc AS gradc1,"
            " B1.field AS field1,"
            " B1.setup AS setup1,"
            " B1.aterm AS aterm1,"
            " B2.place AS place2,"
            " B2.gradc AS gradc2,"
            " B2.field AS field2,"
            " B2.setup AS setup2,"
            " B2.aterm AS aterm2 "
            "FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " aterm1 = ?"
            " AND"
            " aterm1 = aterm2"
            " AND"
            " place1 = place2"
            " AND"
            " setup1 REGEXP ?"
            " AND"
            " setup2 REGEXP ?"
            " AND"
            " setup1 != setup2",
            [SEMESTER, RE["HPW"]["4"]["A"], RE["HPW"]["4"]["A"]],
        ).fetchall()
        # }}}
    elif HPW == 10:
        # HPW10 {{{
        choices = CURSOR.execute(
            "SELECT"
            " B1.place AS place1,"
            " B1.gradc AS gradc1,"
            " B1.field AS field1,"
            " B1.setup AS setup1,"
            " B1.aterm AS aterm1,"
            " B2.place AS place2,"
            " B2.gradc AS gradc2,"
            " B2.field AS field2,"
            " B2.setup AS setup2,"
            " B2.aterm AS aterm2 "
            "FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " aterm1 = ?"
            " AND"
            " aterm1 = aterm2"
            " AND"
            " place1 = place2"
            " AND"
            " setup1 REGEXP ?"
            " AND"
            " setup2 REGEXP ?"
            " AND"
            " setup1 != setup2",
            [SEMESTER, RE["HPW"]["4"]["A"], RE["HPW"]["6"]["A"]],
        ).fetchall()
        # }}}
    elif HPW == 12:
        # HPW12 {{{
        choices_p1 = CURSOR.execute(
            "SELECT"
            " B1.place AS place1,"
            " B1.gradc AS gradc1,"
            " B1.field AS field1,"
            " B1.setup AS setup1,"
            " B1.aterm AS aterm1,"
            " B2.place AS place2,"
            " B2.gradc AS gradc2,"
            " B2.field AS field2,"
            " B2.setup AS setup2,"
            " B2.aterm AS aterm2 "
            "FROM blob AS B1 CROSS JOIN blob as B2 WHERE"
            " B1.aterm = ?"
            " AND"
            " B1.aterm = B2.aterm"
            " AND"
            " B1.place = B2.place"
            " AND"
            " B1.setup REGEXP ?"
            " AND"
            " B2.setup REGEXP ?"
            " AND"
            " B1.setup != B2.setup",
            [SEMESTER, RE["HPW"]["6"]["A"], RE["HPW"]["6"]["A"]],
        ).fetchall()
        choices_p2 = CURSOR.execute(
            "SELECT"
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  J23.place2 AS place2,"
            "  J23.gradc2 AS gradc2,"
            "  J23.field2 AS field2,"
            "  J23.setup2 AS setup2,"
            "  J23.aterm2 AS aterm2,"
            "  J23.place3 AS place3,"
            "  J23.gradc3 AS gradc3,"
            "  J23.field3 AS field3,"
            "  J23.setup3 AS setup3,"
            "  J23.aterm3 AS aterm3 "
            "FROM blob AS B1 CROSS JOIN("
            "  SELECT"
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
            "    aterm2 = ?"
            "    AND"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3"
            "    AND"
            "    setup2 REGEXP ?"
            "    AND"
            "    setup3 REGEXP ?"
            "    AND"
            "    setup2 != setup3"
            ") AS J23 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup1 != setup2"
            "  AND"
            "  setup1 != setup3",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"],
                SEMESTER,
                RE["HPW"]["4"]["A"],
            ],
        ).fetchall()
        choices = choices_p1 + choices_p2
        # }}}
    elif HPW == 14:
        # HPW14 {{{
        choices = CURSOR.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  J23.place2 AS place2,"
            "  J23.gradc2 AS gradc2,"
            "  J23.field2 AS field2,"
            "  J23.setup2 AS setup2,"
            "  J23.aterm2 AS aterm2,"
            "  J23.place3 AS place3,"
            "  J23.gradc3 AS gradc3,"
            "  J23.field3 AS field3,"
            "  J23.setup3 AS setup3,"
            "  J23.aterm3 AS aterm3 "
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
            "    aterm2 = ?"
            "    AND"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3"
            "    AND"
            "    setup2 REGEXP ?"
            "    AND"
            "    setup3 REGEXP ?"
            "    AND"
            "    setup2 != setup3"
            ") AS J23 "
            "WHERE"
            "  aterm1 = ?"
            "  AND"
            "  aterm1 = aterm2"
            "  AND"
            "  place1 = place2"
            "  AND"
            "  setup1 REGEXP ?"
            "  AND"
            "  setup1 != setup2"
            "  AND"
            "  setup1 != setup3",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"],
                SEMESTER,
                RE["HPW"]["6"]["A"],
            ],
        ).fetchall()
        # }}}
    elif HPW == 16:
        # HPW16 {{{
        choices_p1 = CURSOR.execute(
            "SELECT"
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  J234.place2 AS place2,"
            "  J234.gradc2 AS gradc2,"
            "  J234.field2 AS field2,"
            "  J234.setup2 AS setup2,"
            "  J234.aterm2 AS aterm2,"
            "  J234.place3 AS place3,"
            "  J234.gradc3 AS gradc3,"
            "  J234.field3 AS field3,"
            "  J234.setup3 AS setup3,"
            "  J234.aterm3 AS aterm3,"
            "  J234.place4 AS place4,"
            "  J234.gradc4 AS gradc4,"
            "  J234.field4 AS field4,"
            "  J234.setup4 AS setup4,"
            "  J234.aterm4 AS aterm4 "
            "FROM blob as B1 CROSS JOIN("
            "  SELECT"
            "    B2.place AS place2,"
            "    B2.gradc AS gradc2,"
            "    B2.field AS field2,"
            "    B2.setup AS setup2,"
            "    B2.aterm AS aterm2,"
            "    J34.place3 AS place3,"
            "    J34.gradc3 AS gradc3,"
            "    J34.field3 AS field3,"
            "    J34.setup3 AS setup3,"
            "    J34.aterm3 AS aterm3,"
            "    J34.place4 AS place4,"
            "    J34.gradc4 AS gradc4,"
            "    J34.field4 AS field4,"
            "    J34.setup4 AS setup4,"
            "    J34.aterm4 AS aterm4"
            "  FROM blob AS B2 CROSS JOIN("
            "    SELECT"
            "      B3.place AS place3,"
            "      B3.gradc AS gradc3,"
            "      B3.field AS field3,"
            "      B3.setup AS setup3,"
            "      B3.aterm AS aterm3,"
            "      B4.place AS place4,"
            "      B4.gradc AS gradc4,"
            "      B4.field AS field4,"
            "      B4.setup AS setup4,"
            "      B4.aterm AS aterm4"
            "    FROM blob AS B3 CROSS JOIN blob AS B4"
            "    WHERE"
            "      aterm3 = ?"
            "    AND"
            "      aterm3 = aterm4"
            "    AND"
            "      place3 = place4"
            "    AND"
            "      setup3 REGEXP ?"
            "    AND"
            "      setup4 REGEXP ?"
            "    AND"
            "      setup3 != setup4"
            "  ) AS J34"
            "  WHERE"
            "    aterm2 = ?"
            "  AND"
            "    aterm2 = aterm3"
            "  AND"
            "    place2 = place3"
            "  AND"
            "    setup2 REGEXP ?"
            "  AND"
            "    setup2 != setup3"
            "  AND"
            "    setup2 != setup4"
            ") AS J234 "
            "WHERE"
            "  aterm1 = ? "
            "AND "
            "  aterm1 = aterm2 "
            "AND "
            "  place1 = place2 "
            "AND "
            "  setup1 REGEXP ?"
            "AND "
            "  setup1 != setup2 "
            "AND "
            "  setup1 != setup3 "
            "AND "
            "  setup1 != setup4",
            [
                SEMESTER,
                RE["HPW"]["4"]["A"],
                RE["HPW"]["4"]["A"],
                SEMESTER,
                RE["HPW"]["4"]["A"],
                SEMESTER,
                RE["HPW"]["4"]["A"],
            ]
        ).fetchall()
        choices_p2 = CURSOR.execute(
            "SELECT "
            "  B1.place AS place1,"
            "  B1.gradc AS gradc1,"
            "  B1.field AS field1,"
            "  B1.setup AS setup1,"
            "  B1.aterm AS aterm1,"
            "  J23.place2 AS place2,"
            "  J23.gradc2 AS gradc2,"
            "  J23.field2 AS field2,"
            "  J23.setup2 AS setup2,"
            "  J23.aterm2 AS aterm2,"
            "  J23.place3 AS place3,"
            "  J23.gradc3 AS gradc3,"
            "  J23.field3 AS field3,"
            "  J23.setup3 AS setup3,"
            "  J23.aterm3 AS aterm3 "
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
            "    aterm2 = ?"
            "    AND"
            "    aterm2 = aterm3"
            "    AND"
            "    place2 = place3"
            "    AND"
            "    setup2 REGEXP ?"
            "    AND"
            "    setup3 REGEXP ?"
            "    AND"
            "    setup2 != setup3"
            ") AS J23 "
            "WHERE"
            "  aterm1 = ? "
            "AND"
            "  aterm1 = aterm2 "
            "AND"
            "  place1 = place2 "
            "AND"
            "  setup1 REGEXP ? "
            "AND"
            "  setup1 != setup2 "
            "AND"
            "  setup1 != setup3",
            [
                SEMESTER,
                RE["HPW"]["6"]["A"],
                RE["HPW"]["6"]["A"],
                SEMESTER,
                RE["HPW"]["4"]["A"],
            ],
        ).fetchall()
        choices = choices_p1 + choices_p2
        # }}}
    else:
        choices = None
    return choices


def main():
    with sqlite3.connect("data/sql/sqlite.db") as connection:
        connection.create_function("REGEXP", 2, REGEXP)
        cursor = connection.cursor()

        choices = CHOICES(cursor, CURRENT_SEMESTER(), 12)

    with open("choices.txt", "w") as CFILE:
        print(choices, file=CFILE)


if __name__ == "__main__":
    main()
