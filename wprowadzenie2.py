def function_1(a_list , b_list):
    lista_3 = []
    for i in range(0, len(a_list )):
        if i % 2:
            lista_3.append(a_list [i])
    for i in range(0, len(b_list)):
        if not i % 2:
            lista_3.append(b_list[i])
    return lista_3


a_list  = [i for i in range(1, 16)]
b_list = [i for i in range(23, 39)]
print(function_1(a_list , b_list))


#---------------------------------------------

def function_2(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Dzbany"
print(function_2(data_text))

#----------------------------------------------
