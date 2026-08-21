"""
py_graph_cycle_detector - version simplifiee pour examen

ASTUCE (comptage des "entrees", aucune recursion, 1 seule fonction) :
    Pour chaque noeud, on compte son "degre entrant" = le nombre de
    fleches qui arrivent vers lui.
    On part des noeuds qui n'ont AUCUNE entree (degre 0) : ce sont ceux
    qu'on peut "traiter" en premier sans dependre de personne.
    On les traite un par un : a chaque fois qu'on traite un noeud, on
    enleve ses fleches sortantes, donc on diminue le degre de ses
    voisins. Des qu'un voisin tombe a 0, on peut le traiter a son tour.

    A la fin :
    - si on a reussi a traiter TOUS les noeuds -> pas de cycle.
    - s'il en reste qu'on n'a jamais pu traiter (ils attendaient tous
      les uns sur les autres) -> il y a un cycle.

    Un noeud qui pointe sur lui-meme (0 -> 0) a un degre entrant de 1
    des le depart -> il ne sera jamais traite -> cycle detecte.
"""


def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    noeuds = set(graph.keys())
    for voisins in graph.values():
        for voisin in voisins:
            noeuds.add(voisin)

    degre_entrant = {}
    for noeud in noeuds:
        degre_entrant[noeud] = 0

    for noeud in graph:
        for voisin in graph[noeud]:
            degre_entrant[voisin] += 1

    file = []
    for noeud in noeuds:
        if degre_entrant[noeud] == 0:
            file.append(noeud)

    traites = 0
    tete = 0
    while tete < len(file):
        noeud = file[tete]
        tete += 1
        traites += 1
        for voisin in graph.get(noeud, []):
            degre_entrant[voisin] -= 1
            if degre_entrant[voisin] == 0:
                file.append(voisin)

    return traites != len(noeuds)


if __name__ == "__main__":
    tests = [
        ({0: [1], 1: [2], 2: [0]}, True),
        ({0: [1], 1: [2], 2: []}, False),
        ({0: [1, 2], 1: [3], 2: [3], 3: []}, False),
        ({0: [0]}, True),
        ({}, False),
        ({0: [1], 1: [2], 2: [3], 3: [1]}, True),
        ({0: [], 1: [], 2: []}, False),
    ]

    for graphe, attendu in tests:
        obtenu = graph_cycle_detector(graphe)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} graph_cycle_detector({graphe}) -> {obtenu}",
              f"(attendu: {attendu})")
