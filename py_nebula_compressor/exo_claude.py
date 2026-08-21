"""
py_nebula_compressor - version simplifiee pour examen

ASTUCE (RLE = run-length encoding), tout dans UNE seule fonction :

    Compression :
        - on regroupe les caracteres identiques qui se suivent et on
          compte combien il y en a (variable "longueur").
        - 1 seul caractere      -> on l'ecrit tel quel
        - 2 a 9 fois            -> "caractere" + "nombre"
        - 10 fois ou plus       -> on decoupe en paquets de 9 max
          (13 'a' -> "a9a4", car 9 + 4 = 13)

    Decompression :
        - on lit caractere par caractere.
        - si le caractere suivant est un chiffre, on repete le
          caractere courant ce nombre de fois.
        - sinon, le caractere ne compte qu'une seule fois.
"""


def nebula_compressor(operation: str, data: str) -> str:
    resultat = ""

    if operation == "compress":
        i = 0
        while i < len(data):
            caractere = data[i]
            longueur = 1
            while (i + longueur < len(data)
                    and data[i + longueur] == caractere):
                longueur += 1

            restant = longueur
            while restant > 9:
                resultat += caractere + "9"
                restant -= 9

            if restant == 1:
                resultat += caractere
            else:
                resultat += caractere + str(restant)

            i += longueur

    elif operation == "decompress":
        i = 0
        while i < len(data):
            caractere = data[i]
            if i + 1 < len(data) and data[i + 1].isdigit():
                nombre = int(data[i + 1])
                resultat += caractere * nombre
                i += 2
            else:
                resultat += caractere
                i += 1

    else:
        return "Error"

    return resultat


if __name__ == "__main__":
    tests = [
        (("compress", "aaabbc"), "a3b2c"),
        (("compress", "hello"), "hel2o"),
        (("compress", "aaaaaaaaaaaaa"), "a9a4"),
        (("compress", "abcdef"), "abcdef"),
        (("decompress", "a3b2c"), "aaabbc"),
        (("decompress", "hel2o"), "hello"),
        (("decompress", "a9a4"), "aaaaaaaaaaaaa"),
        (("compress", ""), ""),
        (("decompress", ""), ""),
        (("invalid", "test"), "Error"),
    ]

    for args, attendu in tests:
        obtenu = nebula_compressor(*args)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} nebula_compressor{args} -> {obtenu!r}",
              f"(attendu: {attendu!r})")
