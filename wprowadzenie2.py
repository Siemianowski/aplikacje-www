def function_1(lista_1, lista_2):
    lista_3 = []
    for i in range(0, len(lista_1)):
        if i % 2:
            lista_3.append(lista_1[i])
    for i in range(0, len(lista_2)):
        if not i % 2:
            lista_3.append(lista_2[i])
    return lista_3


lista_1 = [i for i in range(1, 16)]
lista_2 = [i for i in range(23, 39)]
print(function_1(lista_1, lista_2))


#---------------------------------------------

def function_2(tekst):
    return {'length': len(tekst),
            'letters': list(set(list(tekst))),
            'big_letters': tekst.upper(),
            'small_letters': tekst.lower(),
            }


tekst = "Dzbany"
print(function_2(tekst))

#----------------------------------------------
