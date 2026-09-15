from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict est un dictionnaire qui retient l'ordre dans
        # lequel les cles ont ete inserees ou deplacees. Le premier
        # element de cet ordre est donc toujours le moins recemment
        # utilise : c'est lui qu'on eliminera en cas de depassement.
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # La cle vient d'etre consultee : on la deplace en derniere
        # position pour marquer qu'elle est desormais la plus recente.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # La cle existe deja : on la deplace en derniere position
            # avant de mettre sa valeur a jour.
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # On a depasse la capacite : on retire le premier element
            # de l'ordre, c'est-a-dire le moins recemment utilise.
            self.cache.popitem(last=False)


if __name__ == "__main__":
    # Test 1 : exemple exact du sujet
    cache = LRUCache(2)
    cache.put(1, 1)                    # cache = {1: 1}
    cache.put(2, 2)                    # cache = {1: 1, 2: 2}
    assert cache.get(1) == 1           # 1 est utilise, il passe en dernier
    cache.put(3, 3)                    # capacite depassee, on evince 2 (LRU)
    assert cache.get(2) == -1          # 2 a bien ete evince
    cache.put(4, 4)                    # capacite depassee, on evince 1 (LRU)
    assert cache.get(1) == -1          # 1 a bien ete evince
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("Test 1 reussi")

    # Test 2 : mettre a jour une cle existante doit la rafraichir,
    # pas creer une eviction inattendue de cette meme cle
    cache2 = LRUCache(2)
    cache2.put(1, 10)
    cache2.put(2, 20)
    cache2.put(1, 100)                 # 1 est mis a jour, redevient le plus recent
    cache2.put(3, 30)                  # capacite depassee, on evince 2 (LRU), pas 1
    assert cache2.get(1) == 100
    assert cache2.get(2) == -1
    assert cache2.get(3) == 30
    print("Test 2 reussi")

    # Test 3 : capacite de 1, chaque nouvel ajout evince le precedent
    cache3 = LRUCache(1)
    cache3.put(1, 1)
    cache3.put(2, 2)
    assert cache3.get(1) == -1
    assert cache3.get(2) == 2
    print("Test 3 reussi")

    print("Tous les tests sont passes !")
