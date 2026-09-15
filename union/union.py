class UnionFind:
    def __init__(self, n: int):
        # Au depart, chaque element est son propre parent : il forme
        # a lui seul son propre ensemble. parent[i] == i tant qu'il
        # n'a ete fusionne avec personne.
        self.parent = list(range(n))
        # Le rang approxime la hauteur de l'arbre de chaque ensemble.
        # Il sert uniquement a decider qui devient parent de qui lors
        # d'une union, pour garder les arbres les plus plats possibles.
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Tant que x n'est pas la racine de son propre ensemble,
        # on remonte vers son parent.
        if self.parent[x] != x:
            # Compression de chemin : une fois la racine trouvee, on
            # fait pointer x directement dessus. Les prochains appels
            # a find(x) seront donc immediats.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        # Meme racine => x et y sont deja dans le meme ensemble,
        # il n'y a rien a fusionner.
        if root_x == root_y:
            return False

        # Union par rang : on accroche toujours l'arbre le moins haut
        # sous l'arbre le plus haut, pour eviter de creer une longue
        # chaine qui ralentirait les futurs find().
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x

        # Si les deux arbres avaient la meme hauteur, le resultat de
        # la fusion est un cran plus haut qu'avant.
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

    def connected(self, x: int, y: int) -> bool:
        # x et y sont dans le meme ensemble si et seulement si ils
        # ont la meme racine.
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    # Test 1 : premier exemple du sujet (5 elements)
    uf = UnionFind(5)
    assert uf.connected(0, 1) == False   # rien n'est encore relie
    assert uf.union(0, 1) == True        # fusion reussie
    assert uf.connected(0, 1) == True    # maintenant relies
    assert uf.union(1, 2) == True        # fusion reussie
    assert uf.connected(0, 2) == True    # 0, 1, 2 sont dans le meme ensemble
    assert uf.union(0, 1) == False       # deja dans le meme ensemble
    assert uf.find(2) == uf.find(0)      # meme racine pour tout le groupe
    print("Test 1 reussi")

    # Test 2 : deuxieme exemple du sujet (3 elements)
    uf2 = UnionFind(3)
    assert uf2.union(0, 1) == True
    assert uf2.union(1, 2) == True
    assert uf2.connected(0, 2) == True
    assert uf2.find(0) == uf2.find(2)
    print("Test 2 reussi")

    # Test 3 : des elements jamais unis doivent rester dans des
    # ensembles separes
    uf3 = UnionFind(4)
    assert uf3.connected(0, 3) == False
    assert uf3.find(3) == 3
    print("Test 3 reussi")

    # Test 4 : un element seul est toujours connecte a lui-meme
    uf4 = UnionFind(1)
    assert uf4.connected(0, 0) == True
    print("Test 4 reussi")

    print("Tous les tests sont passes !")
