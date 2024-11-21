#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
from datetime import datetime
from itertools import combinations, groupby, product
from operator import itemgetter

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


def CLASSES_ARE_CONSECUTIVE(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    DIGT1 = DIGITS(COMP1[2])
    DIGT2 = DIGITS(COMP2[2])
    COND0 = len([x for x in DIGITS(COMP1[0]) if x in DIGITS(COMP2[0])]) > 0
    COND1 = COMP1[1] == COMP2[1]
    COND2 = (DIGT1[1] + 1 == DIGT2[0]) or (DIGT2[1] + 1 == DIGT1[0])
    return (COND0 and COND1 and COND2)


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

        BLOB = cursor.execute(
            "SELECT place, gradc, field, setup FROM blob"
            " WHERE aterm = ? ORDER BY setup", [SEMESTER]
        ).fetchall()

        for blob in BLOB:
            print(blob)

        CAMPUS = list(
            map(itemgetter(0), groupby(sorted([x[0] for x in BLOB])))
        )

        print(CAMPUS)

        # GRADCOURSE = list(
        #     map(itemgetter(0), groupby(sorted([x[1] for x in BLOB])))
        # )

        # DISCIPLINE = list(
        #     map(itemgetter(0), groupby(sorted([x[2] for x in BLOB])))
        # )

        # TIMETABLE = list(
        #     map(itemgetter(0), groupby(sorted([x[3] for x in BLOB])))
        # )

        # for campus in CAMPUS:
        #     for H in RE["HPW"].keys():
        #         for P in RE["HPW"][H].keys():
        #             QTY = cursor.execute(
        #                 "SELECT COUNT(*) from blob"
        #                 " WHERE semester = ? AND"
        #                 " campus = ? AND timetable REGEXP ?;",
        #                 [SEMESTER, campus, RE["HPW"][H][P]]
        #             ).fetchone()[0]
        #             print(f"{campus}, {P}, {H}, {QTY:2d}")

        # BLOB = cursor.execute(
        #     "SELECT blob.campus, blob.dscpln, blob.timetable, COUNT(*) FROM blob"
        #     " WHERE semester = ?"
        #     " GROUP BY blob.campus, blob.dscpln, blob.timetable;",
        #     [SEMESTER],
        # ).fetchall()

        # X = {
        #     "2": [x[:4] for x in BLOB if RE["HPW"]["2"]["A"].match(x[3])],
        #     "4": [x[:4] for x in BLOB if RE["HPW"]["4"]["A"].match(x[3])],
        #     "6": [x[:4] for x in BLOB if RE["HPW"]["6"]["A"].match(x[3])],
        # }

        # Y = {}

        # Y["8"] = list(combinations(X["4"], 2))

        # Y["10"] = list(product(X["4"], X["6"]))
        # Y["12"] = list(combinations(X["4"], 3)) + list(combinations(X["6"], 2))
        # Y["14"] = list(product(Y["08"], X["6"]))
        # Y["16"] = list(combinations(X["4"], 4)) + list(product(X["4"], Y["12"]))

        # print([y for y in Y["8"] if feasible(2, y) is True])

        # print(Y["8"])


if __name__ == "__main__":
    main()
