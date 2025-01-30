import re
import sqlite3
from datetime import datetime
from typing import Tuple, TypeAlias

Blob: TypeAlias = Tuple[int]
Conn: TypeAlias = sqlite3.Connection


def DEFAULT_SEMESTER() -> str:
    Y = int(datetime.today().strftime("%Y"))
    M = int(datetime.today().strftime("%m"))
    return f"{Y}_2" if (M <= 6) else f"{Y+1}_1"


def SEMESTER(semester: str = DEFAULT_SEMESTER()) -> str:
    RE = re.compile(r"^20(2[5-9]|[3-9][0-9])_[12]$")
    if RE.match(semester):
        S = semester
    else:
        S = DEFAULT_SEMESTER()
    return S


def REGEXP(pattern: str, input: str) -> bool:
    regexp = re.compile(pattern)
    return bool(regexp.match(input))


def NAME(conn: Conn, table: str, pkey: int) -> str | None:
    name = None
    if table in ["campus", "curso", "disciplina", "horario", "semestre"]:
        query = f"SELECT y FROM '{table}' WHERE x = '{pkey}'"
        try:
            result = conn.execute(query)
            if result is not None:
                name = result.fetchone()[0]
        except sqlite3.OperationalError as Err:
            print(f"Operational Error: {Err}")
    return name


def PKEY(conn: Conn, table: str, name: str) -> int | None:
    pkey = None
    if table in ["campus", "curso", "disciplina", "horario", "semestre"]:
        query = f"SELECT x FROM '{table}' WHERE y = '{name}'"
        try:
            result = conn.execute(query)
            if result is not None:
                pkey = result.fetchone()[0]
        except sqlite3.OperationalError as Err:
            print(f"Operational Error: {Err}")
    return pkey


def BLOB(conn: Conn, profile: int, semester=DEFAULT_SEMESTER()) -> list[Blob] | None:
    pkey_semester = PKEY(conn, "semestre", SEMESTER(semester))
    RE = {
        # 4HPW {{{
        "4HPW": r"^[2-6]{2}[mtn][1-6]{2}$",
        # }}}
        # 6HPW {{{
        "6HPW": r"^[2-6]{3}[mtn][1-6]{2}$",
        # }}}
    }
    QUERY = {
        # 2BLOBS {{{
        "2BLOBS": (
            "SELECT"
            "  * "
            "FROM"
            "  blob AS B1 "
            "INNER JOIN"
            "  blob AS B2 "
            "ON"
            "("
            "  ("
            "    ("
            "      B1.campus IN (1, 2)"
            "      AND"
            "      B2.campus IN (1, 2)"
            "    )"
            "    OR"
            "    ("
            "      B1.campus = 3"
            "      AND"
            "      B2.campus = 3"
            "    )"
            "  )"
            "  AND"
            "  ("
            "    B1.horario != B2.horario"
            "  )"
            "  AND"
            "  ("
            "    B1.semestre = B2.semestre"
            "    AND"
            "    B2.semestre = ?"
            "  )"
            ")"
            "WHERE"
            "("
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B1.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B2.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            ")"
            "LIMIT 16384;"
        ),
        # }}}
        # 3BLOBS {{{
        "3BLOBS": (
            "SELECT"
            "  * "
            "FROM"
            "  blob AS B1 "
            "INNER JOIN"
            "  blob AS B2, blob as B3 "
            "ON"
            "("
            "  ("
            "    ("
            "      B1.campus IN (1, 2)"
            "      AND"
            "      B2.campus IN (1, 2)"
            "      AND"
            "      B3.campus IN (1, 2)"
            "    )"
            "    OR"
            "    ("
            "      B1.campus = 3"
            "      AND"
            "      B2.campus = 3"
            "      AND"
            "      B3.campus = 3"
            "    )"
            "  )"
            "  AND"
            "  ("
            "    B1.horario != B2.horario"
            "    AND"
            "    B1.horario != B3.horario"
            "    AND"
            "    B2.horario != B3.horario"
            "  )"
            "  AND"
            "  ("
            "    B1.semestre = B2.semestre"
            "    AND"
            "    B2.semestre = B3.semestre"
            "    AND"
            "    B3.semestre = ?"
            "  )"
            ")"
            "WHERE"
            "("
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B1.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B2.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B3.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            ")"
            "LIMIT 16384;"
        ),
        # }}}
        # 4BLOBS {{{
        "4BLOBS": (
            "SELECT"
            "  * "
            "FROM"
            "  blob AS B1 "
            "INNER JOIN"
            "  blob AS B2, blob as B3, blob as B4 "
            "ON"
            "("
            "  ("
            "    ("
            "      B1.campus IN (1, 2)"
            "      AND"
            "      B2.campus IN (1, 2)"
            "      AND"
            "      B3.campus IN (1, 2)"
            "      AND"
            "      B4.campus IN (1, 2)"
            "    )"
            "    OR"
            "    ("
            "      B1.campus = 3"
            "      AND"
            "      B2.campus = 3"
            "      AND"
            "      B3.campus = 3"
            "      AND"
            "      B4.campus = 3"
            "    )"
            "  )"
            "  AND"
            "  ("
            "    B1.horario != B2.horario"
            "    AND"
            "    B1.horario != B3.horario"
            "    AND"
            "    B1.horario != B4.horario"
            "    AND"
            "    B2.horario != B3.horario"
            "    AND"
            "    B2.horario != B4.horario"
            "    AND"
            "    B3.horario != B4.horario"
            "  )"
            "  AND"
            "  ("
            "    B1.semestre = B2.semestre"
            "    AND"
            "    B2.semestre = B3.semestre"
            "    AND"
            "    B3.semestre = B4.semestre"
            "    AND"
            "    B4.semestre = ?"
            "  )"
            ")"
            "WHERE"
            "("
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B1.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B2.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B3.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            "  AND"
            "  EXISTS"
            "  ("
            "    SELECT"
            "      H.x"
            "    FROM"
            "      horario AS H"
            "    WHERE"
            "      H.x = B4.horario"
            "      AND"
            "      H.y REGEXP ?"
            "  )"
            ")"
            "LIMIT 16384;"
        ),
        # }}}
    }
    if profile == 8:
        # 08HPW {{{
        blob = conn.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["4HPW"], RE["4HPW"]]
        ).fetchall()
        # }}}
    elif profile == 10:
        # 10HPW {{{
        blob = conn.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["4HPW"], RE["6HPW"]]
        ).fetchall()
        # }}}
    elif profile == 12:
        # 12HPW {{{
        blob_1 = conn.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = conn.execute(
            QUERY["2BLOBS"], [pkey_semester, RE["6HPW"], RE["6HPW"]]
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    elif profile == 14:
        # 14HPW {{{
        blob = conn.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["6HPW"]],
        ).fetchall()
        # }}}
    elif profile == 16:
        # 16HPW {{{
        blob_1 = conn.execute(
            QUERY["4BLOBS"],
            [pkey_semester, RE["4HPW"], RE["4HPW"], RE["4HPW"], RE["4HPW"]],
        ).fetchall()
        blob_2 = conn.execute(
            QUERY["3BLOBS"],
            [pkey_semester, RE["4HPW"], RE["6HPW"], RE["6HPW"]],
        ).fetchall()
        blob = blob_1 + blob_2
        # }}}
    else:
        blob = None
    return blob
