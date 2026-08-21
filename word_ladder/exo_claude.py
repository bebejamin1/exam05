"""
word_ladder - Word Ladder (entrainement, cf. LeetCode 127)

ASTUCE : BFS (car on veut le chemin le PLUS COURT).
    - beginWord/endWord/wordList = un graphe : deux mots sont relies s'ils
      ne different que d'une seule lettre.
    - BFS depuis beginWord : le premier moment ou on atteint endWord, on a
      forcement le chemin le plus court.
    - Pour trouver les voisins d'un mot : essayer de changer chaque lettre
      par les 25 autres et voir si le resultat est dans le dictionnaire
      (un set, pour une recherche rapide).
    - On retire un mot du set des qu'on le visite, pour ne jamais y
      repasser (evite les boucles infinies).
    - "file" contient des couples (mot, longueur de la sequence pour y
      arriver).
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def word_ladder_length(
    begin_word: str, end_word: str, word_list: list[str]
) -> int:
    mots_dispo = set(word_list)
    if end_word not in mots_dispo:
        return 0

    file = [(begin_word, 1)]
    tete = 0
    mots_dispo.discard(begin_word)

    while tete < len(file):
        mot, longueur = file[tete]
        tete += 1

        if mot == end_word:
            return longueur

        for i in range(len(mot)):
            for lettre in ALPHABET:
                if lettre == mot[i]:
                    continue
                voisin = mot[:i] + lettre + mot[i + 1:]
                if voisin in mots_dispo:
                    mots_dispo.discard(voisin)
                    file.append((voisin, longueur + 1))

    return 0


if __name__ == "__main__":
    tests = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    ]

    for args, attendu in tests:
        obtenu = word_ladder_length(*args)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} word_ladder_length{args} -> {obtenu}",
              f"(attendu: {attendu})")
