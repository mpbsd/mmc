#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from itertools import combinations

# SCHDL {{{
SCHDL = [
    "246M12",
    "246M12",
    "246M23",
    "246M23",
    "246M34",
    "246M34",
    "246M45",
    "246M45",
    "246N23",
    "246N23",
    "246N45",
    "246T12",
    "246T12",
    "246T23",
    "246T34",
    "246T34",
    "246T45",
    "246T56",
    "246T56",
    "24M12",
    "24M12",
    "24M23",
    "24M23",
    "24M34",
    "24M34",
    "24M45",
    "24M45",
    "24M56",
    "24M56",
    "24N23",
    "24N23",
    "24N45",
    "24N45",
    "24T12",
    "24T12",
    "24T23",
    "24T23",
    "24T34",
    "24T45",
    "24T56",
    "24T56",
    "25T23",
    "25T23",
    "25T45",
    "25T45",
    "35M12",
    "35M12",
    "35M23",
    "35M23",
    "35M34",
    "35M34",
    "35M45",
    "35M45",
    "35M56",
    "35N23",
    "35N23",
    "35N34",
    "35N45",
    "35N45",
    "35T12",
    "35T12",
    "35T23",
    "35T34",
    "35T34",
    "35T45",
    "35T45",
    "35T56",
    "36T23",
    "36T23",
    "46M12",
    "46M23",
    "46M23",
    "46M34",
    "46M45",
    "46M45",
    "46M56",
    "46M56",
    "46N23",
    "46N23",
    "46N45",
    "46N45",
    "46T23",
    "46T23",
    "46T34",
    "46T34",
    "46T45",
    "46T45",
    "46T56",
    "56T23",
]
# }}}


def EXPLODE(schdl):
    RE_SCHDL = re.compile(r"^([0-9]+)([MTN])([0-9]+)$")
    return [x for x in RE_SCHDL.split(schdl) if x != ""]


def consecutive(schdl1, schdl2):
    re_digit = re.compile(r"([1-6])")
    expl1 = [x for x in EXPLODE(schdl1) if x != ""]
    expl2 = [x for x in EXPLODE(schdl2) if x != ""]
    C1 = expl1[1] == expl2[1]
    x1, y1 = [x for x in re_digit.split(expl1[2]) if x != ""]
    x2, y2 = [x for x in re_digit.split(expl2[2]) if x != ""]
    C2 = (int(y1) + 1 == int(x2)) or (int(y2) + 1 == int(x1))
    return C1 and C2


def main():
    with open("test.csv", "w") as csvfile:
        for x, y in combinations(SCHDL, 2):
            print(x, y, consecutive(x, y), file=csvfile)


if __name__ == "__main__":
    main()
