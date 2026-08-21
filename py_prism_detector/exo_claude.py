"""
py_prism_detector - version simplifiee pour examen

ASTUCE (force brute, tout dans UNE seule fonction, 4 boucles imbriquees) :
    DIRECTIONS liste les 8 directions (delta_ligne, delta_colonne, code),
    DANS L'ORDRE demande par l'enonce (utile aussi pour trier le
    resultat a la fin, car les tuples se trient naturellement par
    ligne, puis colonne, puis position dans cette liste).

    Pour CHAQUE case (r, c) de la grille, pour CHAQUE direction :
        - on avance pas a pas (dr, dc) en comparant chaque lettre du
          pattern avec la grille.
        - si on sort de la grille OU qu'une lettre ne correspond pas,
          on met "match" a False et on arrete cette direction.
    Si "match" est reste True jusqu'au bout -> on garde (r, c, code).
"""

DIRECTIONS = [
    (0, 1, "H"),
    (0, -1, "H-"),
    (1, 0, "V"),
    (-1, 0, "V-"),
    (1, 1, "D1"),
    (-1, -1, "D1-"),
    (1, -1, "D2"),
    (-1, 1, "D2-"),
]


def prism_detector(
    grid: list[str], pattern: str
) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    rows = len(grid)
    cols = len(grid[0])
    plen = len(pattern)
    resultats = []

    for r in range(rows):
        for c in range(cols):
            for dr, dc, code in DIRECTIONS:
                match = True
                for i in range(plen):
                    rr = r + i * dr
                    cc = c + i * dc
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        match = False
                        break
                    if grid[rr][cc] != pattern[i]:
                        match = False
                        break
                if match:
                    resultats.append((r, c, code))

    return resultats


if __name__ == "__main__":
    tests = [
        ((["ABC", "DEF", "GHI"], "ADG"), [(0, 0, "V")]),
        ((["XYZ", "ABC", "DEF"], "XBF"), [(0, 0, "D1")]),
        (([], "ABC"), []),
        ((["ABC"], ""), []),
    ]

    for (args, attendu) in tests:
        obtenu = prism_detector(*args)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} prism_detector{args} -> {obtenu}",
              f"(attendu: {attendu})")

    print("prism_detector(['HELLO','WORLD'], 'LL') ->",
          prism_detector(["HELLO", "WORLD"], "LL"))
