#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
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


def CLASSES_OCCUR_IN_THE_SAME_PERIOD(timetable1, timetable2):
    COMP1 = COMPONENTS_TIMETABLE(timetable1)
    COMP2 = COMPONENTS_TIMETABLE(timetable2)
    return COMP1[1] == COMP2[1]


def main():
    for choice in CHOICE:
        print(choice)


if __name__ == "__main__":
    main()
