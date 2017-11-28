posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]
def batalla_de_botes(mapa, posiciones_a_disparar):
    botes = [((index + 1), (row.index("b") + 1)) for index, row in enumerate(mapa) if "b" in row]
    for i in range(len(posiciones_a_disparar)):
        botes[i] - posiciones_a_disparar[i]
    return botes


assert (batalla_de_botes(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (batalla_de_botes(["b..","...","..b"],[]) == [(1,1),(3,3)])



[(1,1),(3,4),(1,3),(4,5)]