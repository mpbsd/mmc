#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from pathlib import Path

import pdfplumber
from unidecode import unidecode

disciplinas = re.compile(r"DISCIPLINAS")
campus = re.compile(r"CAMPUS (APARECIDA|COLEMAR|SAMAMBAIA)")
horario = re.compile(r"([0-9]{1,3}[MTN][0-9]{2,4})")


def pdf_exists(PDFfile):
    return Path(PDFfile).is_file()


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


def parse_PDF(PDFfile):
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
                    if (C1 or C2 or C3):
                        stream += C + "\n"
                    else:
                        stream += C + " "
    return stream


def main():
    print(parse_PDF("pdfs/2022-02.pdf"))
    # print(parse_PDF("pdfs/2023-01.pdf"))
    # print(parse_PDF("pdfs/2024-01.pdf"))


if __name__ == "__main__":
    main()
