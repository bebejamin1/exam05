def bridge_finder(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    bridges = []
    disc = {}     # disc[u] = ordre de decouverte de u pendant le parcours
    low = {}      # low[u] = plus petit disc atteignable depuis u en remontant
                  # par des aretes deja vues (retours vers un ancetre)
    visited = set()
    timer = [0]   # utilise une liste car un entier simple ne serait pas
                  # modifiable depuis la fonction dfs imbriquee

    def dfs(u, parent):
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1

        for v in graph.get(u, []):
            if v == parent:
                # On ignore l'arete par laquelle on est arrive : sinon elle
                # serait prise a tort pour une arete de retour vers le pere.
                continue
            if v in visited:
                # v est deja visite : c'est une arete de retour vers un
                # ancetre. Elle permet a u de "remonter" jusqu'a disc[v].
                low[u] = min(low[u], disc[v])
            else:
                dfs(v, u)
                # De retour de l'exploration de v, on propage le meilleur
                # low trouve dans sa sous-branche.
                low[u] = min(low[u], low[v])
                # Si depuis v (et tout ce qui en depend) on ne peut pas
                # remonter plus haut que u, alors couper l'arete (u, v)
                # isolerait v : c'est un pont.
                if low[v] > disc[u]:
                    bridges.append((min(u, v), max(u, v)))

    # Le graphe peut etre non connexe (plusieurs morceaux separes) :
    # on relance un dfs depuis chaque noeud pas encore visite.
    for node in graph:
        if node not in visited:
            dfs(node, -1)

    return sorted(bridges)


if __name__ == "__main__":
    assert bridge_finder({0: [1, 2], 1: [0, 2], 2: [0, 1]}) == []
    print("Test 1 reussi")

    assert bridge_finder({0: [1], 1: [0, 2], 2: [1]}) == [(0, 1), (1, 2)]
    print("Test 2 reussi")

    assert bridge_finder({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}) == [(1, 3)]
    print("Test 3 reussi")

    assert bridge_finder({}) == []
    print("Test 4 reussi")

    assert bridge_finder({0: [1], 1: [0]}) == [(0, 1)]
    print("Test 5 reussi")

    assert bridge_finder({0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1], 3: [1, 4], 4: [1, 3]}) == []
    print("Test 6 reussi")

    # Test supplementaire : graphe non connexe forme de deux composantes
    # separees, chacune avec son propre pont independant.
    assert bridge_finder({0: [1], 1: [0], 2: [3], 3: [2]}) == [(0, 1), (2, 3)]
    print("Test 7 reussi")

    print("Tous les tests sont passes !")
