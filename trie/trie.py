def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    # On garde tous les mots qui commencent par le prefixe. startswith()
    # est deja sensible a la casse, donc "Cat" ne matche pas prefix "c".
    # On utilise un set pour ne garder qu'une seule copie de chaque mot,
    # meme s'il apparait plusieurs fois dans la liste d'entree.
    matches = set()
    for word in words:
        if word.startswith(prefix):
            matches.add(word)

    # sorted() sur un set renvoie une liste triee par ordre alphabetique.
    return sorted(matches)


if __name__ == "__main__":
    assert trie_autocomplete(["apple", "app", "apricot", "banana"], "app") == ["app", "apple"]
    print("Test 1 reussi")

    assert trie_autocomplete(["apple", "app", "apricot", "banana"], "ban") == ["banana"]
    print("Test 2 reussi")

    assert trie_autocomplete(["hello", "world", "help", "heap"], "he") == ["heap", "hello", "help"]
    print("Test 3 reussi")

    assert trie_autocomplete(["test"], "xyz") == []
    print("Test 4 reussi")

    assert trie_autocomplete(["cat", "car", "card", "care"], "car") == ["car", "card", "care"]
    print("Test 5 reussi")

    assert trie_autocomplete([], "test") == []
    print("Test 6 reussi")

    assert trie_autocomplete(["a", "ab", "abc"], "") == ["a", "ab", "abc"]
    print("Test 7 reussi")

    # Test supplementaire : les doublons dans l'entree ne doivent
    # apparaitre qu'une seule fois dans le resultat.
    assert trie_autocomplete(["cat", "cat", "cat"], "c") == ["cat"]
    print("Test 8 reussi")

    # Test supplementaire : la recherche est sensible a la casse.
    assert trie_autocomplete(["Cat", "cat"], "c") == ["cat"]
    print("Test 9 reussi")

    print("Tous les tests sont passes !")
