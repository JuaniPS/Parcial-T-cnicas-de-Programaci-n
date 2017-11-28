assert (batalla_de_botes([],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes([""],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["      "],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (batalla_de_botes(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (batalla_de_botes(["b..","...","..b"],[]) == [(1,1),(3,3)])

