"""
matrix - Spiral Matrix (entrainement, cf. LeetCode 54)

ASTUCE (methode "4 bornes", a retenir par coeur) :
    On garde 4 limites qui se resserrent : haut, bas, gauche, droite.
    Tant que haut <= bas et gauche <= droite, on parcourt dans l'ordre :
        1. la ligne du haut, de gauche a droite      -> puis haut += 1
        2. la colonne de droite, de haut en bas       -> puis droite -= 1
        3. la ligne du bas, de droite a gauche        -> puis bas -= 1
        4. la colonne de gauche, de bas en haut       -> puis gauche += 1
    Les etapes 3 et 4 sont protegees par un "if" car sur une matrice pas
    carree, il peut ne plus rester de ligne/colonne a ce moment-la.
"""


def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    haut = 0
    bas = len(matrix) - 1
    gauche = 0
    droite = len(matrix[0]) - 1
    resultat = []

    while haut <= bas and gauche <= droite:
        for c in range(gauche, droite + 1):
            resultat.append(matrix[haut][c])
        haut += 1

        for r in range(haut, bas + 1):
            resultat.append(matrix[r][droite])
        droite -= 1

        if haut <= bas:
            for c in range(droite, gauche - 1, -1):
                resultat.append(matrix[bas][c])
            bas -= 1

        if gauche <= droite:
            for r in range(bas, haut - 1, -1):
                resultat.append(matrix[r][gauche])
            gauche += 1

    return resultat


if __name__ == "__main__":
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([], []),
    ]

    for matrice, attendu in tests:
        obtenu = spiral_order(matrice)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} spiral_order({matrice}) -> {obtenu}",
              f"(attendu: {attendu})")
