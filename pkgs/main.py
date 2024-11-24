#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from operator import itemgetter
from itertools import groupby, combinations

from data.hpw.twelve import CHOICE



def COMPONENTS_TIMETABLE(timetable):
    RE_TIMETABLE = re.compile(r"^([0-9]+)([MTN])([0-9]+)$")
    return [x for x in RE_TIMETABLE.split(timetable) if x != ""]


def HPW(timetable):
    M = len(COMPONENTS_TIMETABLE(timetable)[0])
    N = len(COMPONENTS_TIMETABLE(timetable)[2])
    return M * N


def INDIVIDUAL_DIGITS(number):
    RE_DIGITS = re.compile(r"([1-6])")
    return sorted([int(x) for x in RE_DIGITS.split(number) if x != ""])


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
    DOW1 = WEEKDAYS(COMP1[0])
    DOW2 = WEEKDAYS(COMP2[0])
    ORD1 = INDIVIDUAL_DIGITS(COMP1[2])
    ORD2 = INDIVIDUAL_DIGITS(COMP2[2])
    COND0 = len([x for x in DOW1 if x in DOW2]) > 0
    COND1 = COMP1[1] == COMP2[1]
    COND2 = (ORD1[1] + 1 == ORD2[0]) or (ORD2[1] + 1 == ORD1[0])
    return COND0 and COND1 and COND2


def CLASSES_OCCUR_IN_THE_SAME_DAYS(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    return COMP1[0] == COMP2[0]


def CLASSES_OCCUR_IN_THE_SAME_PERIOD(choice):
    N = len(choice) // 5
    X = sorted([COMPONENTS_TIMETABLE(choice[5 * i + 3])[1] for i in range(N)])
    return len(list(map(lambda x: itemgetter(0)(x), groupby(X)))) == 1


def DISCIPLINES_THAT_I_LIKE(choice):
    FIELD = [
        1,
        2,
        3,
        4,
        5,
        6,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        32,
        33,
        34,
        37,
        46,
        47,
        48,
    ]
    N = len(choice) // 5
    X = [choice[i * 5 + 2] for i in range(N)]
    return len([x for x in X if x in FIELD]) == N


def OVERLAPPING(choice):
    N = len(choice) // 5
    X = [choice[i * 5 + 3] for i in range(N)]
    B = 1
    for X1, X2 in combinations(X, 2):
        COMP1 = COMPONENTS_TIMETABLE(X1)
        COMP2 = COMPONENTS_TIMETABLE(X2)
        D10 = INDIVIDUAL_DIGITS(COMP1[0])
        D20 = INDIVIDUAL_DIGITS(COMP2[0])
        D11 = INDIVIDUAL_DIGITS(COMP1[2])
        D21 = INDIVIDUAL_DIGITS(COMP2[2])
        C0 = len([x for x in D10 if x in D20]) > 0
        C1 = COMP1[1] == COMP2[1]
        C2 = len([x for x in D11 if x in D21]) > 0
        B *= 1 if (C0 and C1 and C2) else 0
    return True if (B == 1) else False


def main():
    CHC = [
        x
        for x in CHOICE
        if DISCIPLINES_THAT_I_LIKE(x) is True and OVERLAPPING(x) is False
        and CLASSES_OCCUR_IN_THE_SAME_PERIOD(x) is True
    ]

    with open("test.txt", "w") as tfile:
        for choice in CHC:
            print(choice, file=tfile)


if __name__ == "__main__":
    main()
