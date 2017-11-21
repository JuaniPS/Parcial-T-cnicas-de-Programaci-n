def ganador(campeonato):

    for i in campeonato:
        if campeonato[0] > campeonato[3]:
            nombre_equipo_1 += 2
        elif campeonato[0] == campeonato[3]:
            nombre_equipo_1 += 1
            nombre_equipo_2 += 1
        else:
            nombre_equipo_2 += 2
    return

    if equipos[nombre_equipo_1] > equipos[nombre_equipo_2]:
        return nombre_equipo_1
    elif equipos[nombre_equipo_1] < equipos[nombre_equipo_2]:
        return nombre_equipo_2
    else:
        return equipos[]