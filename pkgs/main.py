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


def main():

    # numero de configuracoes
    if len(CHOICE) < 8:
        print("E necessario, no minimo, 8 configuracoes.")

    X = []

    for choice in CHOICE:
        for x in choice:
            X.append(x)

    Y = list(map(lambda x: x[0], groupby(sorted(X))))

    # repeticao de disciplinas
    if len(Y) < len(X):
        print("Nao se deve repetir disciplinas")

    # turno noturno
    if [y for y in Y if RE["N"].match(y[3])] == []:
        print("Deve-se ter ao menos uma disciplina no periodo noturno")

    # turnos distintos
    Z = []

    for y in Y:
        if RE["M"].match(y[3]):
            z = RE["M"].match(y[3]).group(2)
            if z not in Z:
                Z.append(z)
        if RE["T"].match(y[3]):
            z = RE["T"].match(y[3]).group(2)
            if z not in Z:
                Z.append(z)
        if RE["N"].match(y[3]):
            z = RE["N"].match(y[3]).group(2)
            if z not in Z:
                Z.append(z)

    if len(Z) < 2:
        print("Deve-se ter ao menos uma configuracao em turnos distintos")

    # aparecida
    if [y for y in Y if y[0] == "aparecida"] == []:
        print("Deve-se ter ao menos uma configuracao em aparecida")


if __name__ == "__main__":
    main()
