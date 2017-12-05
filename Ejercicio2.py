posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

def batalla_de_botes(mapa, posiciones_a_disparar):

    if any('b' in sublist for sublist in mapa) and len(mapa[0]) == len(mapa[len(mapa) - 1]):
        width = len(mapa[0])
        botes = [((posn // width) + 1, (posn % width) + 1)
                 for posn, elem in enumerate(col for row in mapa for col in row)
                 if elem == "b"]
        resultado = set(botes) - set(posiciones_a_disparar)
        print(posiciones_a_disparar)
        print(botes)
        return resultado
    else:
        return []

'''assert (batalla_de_botes([],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes([""],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["      "],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])'''
print (batalla_de_botes(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba))
'''print(batalla_de_botes(["b..","...","..b"],[]))'''