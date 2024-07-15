#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path

import pdfplumber
from unidecode import unidecode

disciplinas = re.compile(r"DISCIPLINAS")
campus = re.compile(r"CAMPUS (APARECIDA|COLEMAR|SAMAMBAIA)")
horario = re.compile(r"([0-9]{1,3}[MTN][0-9]{2,4})")
separador = re.compile(r"\s*-\s*")
APARECIDA = re.compile(r"CAMPUS APARECIDA(.*)CAMPUS COLEMAR", re.S)
COLEMAR = re.compile(r"CAMPUS COLEMAR(.*)CAMPUS SAMAMBAIA", re.S)
SAMAMBAIA = re.compile(r"CAMPUS SAMAMBAIA(.*)", re.S)


def parsed_row(R):
    return [unidecode(C).upper() for C in R if C not in ["", None]]


def parsed_table(T):
    return [parsed_row(R) for R in T]


def row_should_not_be_excluded(R):
    blacklist = [
        "MANHA",
        "TARDE",
        "NOITE",
        "MATUTINO",
        "VESPERTINO",
        "NOTURNO",
    ]
    should_not_be_excluded = True
    if R == []:
        should_not_be_excluded = False
    else:
        for text_obj in blacklist:
            if text_obj in parsed_row(R):
                should_not_be_excluded = False
    return should_not_be_excluded


def parse_PDF(ano, semestre):
    PDFfile = f"pdfs/{ano}-{semestre}.pdf"
    CSVfile = f"brew/{ano}-{semestre}.csv"
    if Path(PDFfile).is_file():
        stream = ""
        with pdfplumber.open(PDFfile) as PDF:
            N = len(PDF.pages)
            for i in range(N):
                table = [
                    R
                    for R in parsed_table(PDF.pages[i].extract_table())
                    if row_should_not_be_excluded(R)
                ]
                for R in table:
                    for C in R:
                        C1 = disciplinas.search(C)
                        C2 = campus.search(C)
                        C3 = horario.match(C)
                        if C1 or C2 or C3:
                            stream += C + "\n"
                        else:
                            stream += C + " "
        stream = separador.sub(r";", stream)
        aparecida = re.sub(
            r"([0-9]{1,3}[MTN][0-9]{2,4})",
            r"\1;APARECIDA",
            APARECIDA.search(stream).group(0),
        )
        colemar = re.sub(
            r"([0-9]{1,3}[MTN][0-9]{2,4})",
            r"\1;COLEMAR",
            COLEMAR.search(stream).group(0),
        )
        samambaia = re.sub(
            r"([0-9]{1,3}[MTN][0-9]{2,4})",
            r"\1;SAMAMBAIA",
            SAMAMBAIA.search(stream).group(0),
        )
        with open(CSVfile, "w") as CSV:
            print(aparecida + colemar + samambaia, file=CSV)


def main():
    parse_PDF("2024", "01")


if __name__ == "__main__":
    main()
