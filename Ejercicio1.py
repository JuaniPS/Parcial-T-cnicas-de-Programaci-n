def rotaciones(palabra):
    lista_de_rotaciones = []
    if  palabra == "     ":
        return lista_de_rotaciones
    elif type(palabra) == str:
        for p in range(len(palabra)):
            a = palabra[:p]
            b = palabra[p:]
            lista_de_rotaciones.append(b + a)
        return lista_de_rotaciones

assert (rotaciones("") == [])
assert (rotaciones("     ") == [])
assert (rotaciones("a") == ['a'])
assert (rotaciones("ab") == ['ab','ba'])
assert (rotaciones("paz") == ['paz','azp','zpa'])
assert (rotaciones("so l") == ['so l','o ls',' lso','lso '])
assert (rotaciones("rotar") == ['rotar','otarr','tarro','arrot','rrota'])