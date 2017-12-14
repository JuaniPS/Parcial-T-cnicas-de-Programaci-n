def ganador(campeonato):

    equipos = {}

    if campeonato == []:
        return ""

    for p in campeonato:
        if p[0] not in campeonato:
            equipos[p[0]] = 0
        if p[2] not in campeonato:
            equipos[p[2]] = 0

    for p in campeonato:
        if p[1] > p[3]:
            equipos[p[0]] += 2
        elif p[3] > p[1]:
            equipos[p[2]] += 2
        else:
            equipos[p[0]] += 1
            equipos[p[2]] += 1

    lideres = []

    campeon = max(equipos, key=equipos.get)
    lideres.append(campeon)

    for e in equipos:
        if equipos[e] == equipos[campeon] and e not in lideres:
            lideres.append(e)

    lideres = sorted(lideres)

    return lideres[0]


assert (ganador([]) == "")
assert (ganador([("a", 1, "b", 0)]) == "a")
assert (ganador([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ganador([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ganador([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")