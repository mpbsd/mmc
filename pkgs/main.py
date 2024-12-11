#!/usr/bin/env python3

import re
from itertools import groupby


# REGEXP {{{
RE = {
    "M": re.compile(r"^([2-6]{1,3})(m)([1-6]{1,3})$"),
    "T": re.compile(r"^([2-6]{1,3})(t)([1-6]{1,3})$"),
    "N": re.compile(r"^([2-6]{1,3})(n)([1-6]{1,3})$"),
}
# }}}
# CHOICE {{{
CHOICE = [
    [
        (
            "samambaia",
            "inteligencia artificial",
            "calculo 1a",
            "246m45",
            "2024_2",
        ),
        ("samambaia", "quimica bacharelado", "calculo 1a", "246m23", "2024_2"),
    ],
    [
        ("samambaia", "quimica bacharelado", "calculo 1a", "246m23", "2024_2"),
        (
            "samambaia",
            "inteligencia artificial",
            "calculo 1a",
            "246m45",
            "2024_2",
        ),
    ],
    [
        (
            "samambaia",
            "ciencia da computacao",
            "calculo 2a",
            "246m45",
            "2024_2",
        ),
        (
            "samambaia",
            "engenharia de alimentos",
            "calculo 2a",
            "246m23",
            "2024_2",
        ),
    ],
    [
        (
            "samambaia",
            "ciencia da computacao",
            "calculo 2a",
            "246m45",
            "2024_2",
        ),
        ("samambaia", "engenharia quimica", "calculo 2a", "246m23", "2024_2"),
    ],
    [
        (
            "samambaia",
            "engenharia de alimentos",
            "calculo 2a",
            "246m23",
            "2024_2",
        ),
        (
            "samambaia",
            "ciencia da computacao",
            "calculo 2a",
            "246m45",
            "2024_2",
        ),
    ],
    [
        ("samambaia", "engenharia quimica", "calculo 2a", "246m23", "2024_2"),
        (
            "samambaia",
            "ciencia da computacao",
            "calculo 2a",
            "246m45",
            "2024_2",
        ),
    ],
    [
        (
            "samambaia",
            "inteligencia artificial",
            "calculo 1a",
            "246m45",
            "2024_2",
        ),
        (
            "samambaia",
            "engenharia de alimentos",
            "calculo 2a",
            "246m23",
            "2024_2",
        ),
    ],
    [
        (
            "samambaia",
            "inteligencia artificial",
            "calculo 1a",
            "246m45",
            "2024_2",
        ),
        ("samambaia", "engenharia quimica", "calculo 2a", "246m23", "2024_2"),
    ],
]
# }}}


def checkhealth(choice):
    error = []

    # numero de configuracoes
    if len(CHOICE) < 8:
        error.append(10)

    X = []

    for choice in CHOICE:
        for x in choice:
            X.append(x)

    Y = list(map(lambda x: x[0], groupby(sorted(X))))

    # repeticao de disciplinas
    if len(Y) < len(X):
        error.append(11)

    # turno noturno
    if [y for y in Y if RE["N"].match(y[3])] == []:
        error.append(12)

    # turnos distintos
    Z = {
        "M": [RE["M"].match(y[3]).group(2) for y in Y if RE["M"].match(y[3])],
        "T": [RE["T"].match(y[3]).group(2) for y in Y if RE["T"].match(y[3])],
        "N": [RE["N"].match(y[3]).group(2) for y in Y if RE["N"].match(y[3])],
    }

    if len([t for t in Z.keys() if Z[t] != []]):
        error.append(13)

    # aparecida
    if [y for y in Y if y[0] == "aparecida"] == []:
        error.append(14)

    return error


def main():

    code = {
        10: "Não há configurações em quantidade suficiente",
        11: "Há disciplinas repetidas",
        12: "Não há disciplinas no período noturno",
        13: "Não há diversidade de turnos",
        14: "Não há disciplinas em Aparecida de Goiânia",
    }

    print(checkhealth(CHOICE))



if __name__ == "__main__":
    main()
