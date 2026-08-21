"""
py_meeting_room_scheduler - version simplifiee pour examen

ASTUCE LA PLUS SIMPLE :
    1. Trier les reunions par heure de DEBUT.
    2. Pour chaque reunion, regarder les salles DEJA ouvertes une par une
       (dans l'ordre) : si la derniere reunion de cette salle est finie
       avant (ou pile) le debut de la nouvelle -> on la met dans cette
       salle.
    3. Si aucune salle n'est libre -> on ouvre une nouvelle salle.

    Pas besoin de retrier une liste de salles par heure de fin : on veut
    juste savoir "existe-t-il une salle libre ?", peu importe laquelle.
    Si toutes sont occupees -> il en faut forcement une de plus.
"""


def meeting_room_scheduler(meetings: list[list[int]]) -> dict[str, any]:
    if not meetings:
        return {"rooms_needed": 0, "room_assignments": {}}

    meetings = sorted(meetings, key=lambda m: m[0])
    room_assignments: dict[int, list[list[int]]] = {}

    for debut, fin in meetings:
        placee = False
        for reunions in room_assignments.values():
            if reunions[-1][1] <= debut:
                reunions.append([debut, fin])
                placee = True
                break
        if not placee:
            room_assignments[len(room_assignments)] = [[debut, fin]]

    return {
        "rooms_needed": len(room_assignments),
        "room_assignments": room_assignments,
    }


if __name__ == "__main__":
    tests = [
        (
            [[0, 30], [5, 10], [15, 20]],
            {
                "rooms_needed": 2,
                "room_assignments": {0: [[0, 30]], 1: [[5, 10], [15, 20]]},
            },
        ),
        (
            [[9, 10], [9, 12], [11, 13]],
            {
                "rooms_needed": 2,
                "room_assignments": {0: [[9, 10], [11, 13]], 1: [[9, 12]]},
            },
        ),
        (
            [[1, 5], [8, 9], [8, 9]],
            {
                "rooms_needed": 2,
                "room_assignments": {0: [[1, 5], [8, 9]], 1: [[8, 9]]},
            },
        ),
        ([], {"rooms_needed": 0, "room_assignments": {}}),
        (
            [[1, 2], [3, 4], [5, 6]],
            {
                "rooms_needed": 1,
                "room_assignments": {0: [[1, 2], [3, 4], [5, 6]]},
            },
        ),
    ]

    for meetings, attendu in tests:
        obtenu = meeting_room_scheduler(meetings)
        statut = "OK" if obtenu == attendu else "FAIL"
        print(f"{statut} meeting_room_scheduler({meetings})")
        print(f"     -> {obtenu}")
        if obtenu != attendu:
            print(f"     attendu: {attendu}")
