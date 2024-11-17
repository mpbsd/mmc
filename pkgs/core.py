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


def semester():
    y = datetime.today().strftime("%Y")
    m = datetime.today().strftime("%m")
    return f"{y}_1" if int(m) < 7 else f"{y}_2"


def REGEXP(pattern, input):
    regexp = re.compile(pattern)
    return bool(regexp.match(input))


def HPW(schdl):
    hpw = [x for x in RE["HPW"].keys() if RE["HPW"][x]["A"].match(schdl[3])][0]
    return hpw


def consecutive(schdl1, schdl2):
    re_digit = re.compile(r"([1-6])")
    expl1 = [x for x in EXPLODE(schdl1) if x != ""]
    expl2 = [x for x in EXPLODE(schdl2) if x != ""]
    C1 = expl1[1] == expl2[1]
    x1, y1 = [x for x in re_digit.split(expl1[2]) if x != ""]
    x2, y2 = [x for x in re_digit.split(expl2[2]) if x != ""]
    C2 = (int(y1) + 1 == int(x2)) or (int(y2) + 1 == int(x1))
    return (C1 and C2)


def main():
    SEMESTER = semester()

    with sqlite3.connect("data/sqlite.db") as connection:
        connection.create_function("REGEXP", 2, REGEXP)
        cursor = connection.cursor()

        BLOB = cursor.execute(
            "SELECT * FROM blob WHERE semester = ?", [SEMESTER]
        ).fetchall()

        CAMPUS = list(
            map(itemgetter(0), groupby(sorted([x[0] for x in BLOB])))
        )

        # GRADCOURSE = list(
        #     map(itemgetter(0), groupby(sorted([x[1] for x in BLOB])))
        # )

        # DISCIPLINE = list(
        #     map(itemgetter(0), groupby(sorted([x[2] for x in BLOB])))
        # )

        # TIMETABLE = list(
        #     map(itemgetter(0), groupby(sorted([x[3] for x in BLOB])))
        # )

        for campus in CAMPUS:
            for H in RE["HPW"].keys():
                for P in RE["HPW"][H].keys():
                    QTY = cursor.execute(
                        "SELECT COUNT(*) from blob"
                        " WHERE semester = ? AND"
                        " campus = ? AND schdl REGEXP ?;",
                        [SEMESTER, campus, RE["HPW"][H][P]]
                    ).fetchone()[0]
                    print(f"{campus}, {P}, {H}, {QTY:2d}")

        # BLOB = cursor.execute(
        #     "SELECT blob.campus, blob.dscpln, blob.schdl, COUNT(*) FROM blob"
        #     " WHERE semester = ?"
        #     " GROUP BY blob.campus, blob.dscpln, blob.schdl;",
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
