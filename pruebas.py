def ganador(campeonato):

    equipos = []

    for i in campeonato:
        if not i[0] in equipos:
            equipos.append(i[0])
        elif not i[2] in equipos:
            equipos.append(i[2])
    return equipos










print(ganador([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]))