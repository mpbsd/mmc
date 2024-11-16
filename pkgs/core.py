#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
from datetime import datetime
from itertools import groupby
from operator import itemgetter


def semester():
    y = datetime.today().strftime("%Y")
    m = datetime.today().strftime("%m")
    return f"{Y}_1" if int(m) < 7 else f"{y}_2"


def regexp(pattern, input):
    exp = re.compile(pattern)
    return bool(exp.match(input))


def main():
    SEMESTER = semester()

    # RE_SCHEDULE {{{
    RE_SCHEDULE = {
        "HPW": {
            "2": {
                "M": r"^[0-9]M[0-9]+$",
                "T": r"^[0-9]T[0-9]+$",
                "N": r"^[0-9]N[0-9]+$",
            },
            "4": {
                "M": r"^[0-9]{2}M[0-9]{2}$",
                "T": r"^[0-9]{2}T[0-9]{2}$",
                "N": r"^[0-9]{2}N[0-9]{2}$",
            },
            "6": {
                "M": r"^[0-9]{3}M[0-9]{2}$",
                "T": r"^[0-9]{3}T[0-9]{2}$",
                "N": r"^[0-9]{3}N[0-9]{2}$",
            },
        }
    }
    # }}}

    with sqlite3.connect("data/sqlite.db") as connection:
        connection.create_function("REGEXP", 2, regexp)
        cursor = connection.cursor()

        # BLOB = cursor.execute(
        #     "SELECT * FROM blob WHERE semester = ?", [SEMESTER]
        # ).fetchall()

        # CAMPUS = list(
        #     map(itemgetter(0), groupby(sorted([x[0] for x in BLOB])))
        # )

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
        #     for H in RE_SCHEDULE["HPW"].keys():
        #         for P in RE_SCHEDULE["HPW"][H].keys():
        #             QTY = cursor.execute(
        #                 "SELECT COUNT(*) from blob WHERE semester = ? AND"
        #                 " campus = ? AND schdl REGEXP ?;",
        #                 [SEMESTER, campus, RE_SCHEDULE["HPW"][H][P]]
        #             ).fetchone()[0]
        #             print(f"{campus}, {P}, {H}, {QTY:2d}")

        OPTS = cursor.execute(
            "SELECT blob.campus, blob.dscpln, blob.schdl, COUNT(*)"
            " FROM blob WHERE semester = ?"
            " GROUP BY blob.campus, blob.dscpln, blob.schdl;",
            [SEMESTER],
        ).fetchall()

        for opt in OPTS:
            if opt[1] == 1:
                print(opt)


if __name__ == "__main__":
    main()
