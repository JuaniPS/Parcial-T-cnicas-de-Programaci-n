def batalla_de_botes(mapa, posiciones_a_disparar):
    botes = [((index + 1), (row.index("b") + 1)) for index, row in enumerate(mapa) if "b" in row]
    for i in range(max(len(botes), len(posiciones_a_disparar))):
        botes[i] - posiciones_a_disparar[i]
    return botes

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

print(batalla_de_botes(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])



for i in range(max(len(botes), len(posiciones_a_disparar))):
    botes.remove(posiones_a_disparar[i])

