#cw1---------------------------------------------
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


#cw2---------------------------------------------

def function_2(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Dzbany"
print(function_2(data_text))

#cw3----------------------------------------------
def funtion_3(text, letter):
    return text.lower().replace(letter.lower(), "")


text = "Paweł weźmiesz mnie do pracy"
letter = "P"
print(my_function(text, letter))

#cw4-----------------------------------------------
def function_4(temperature, temperature_type):
    temp = 0
    # if params valid
    if temperature < -273:
        return Exception("Temperatura nie istnieje")
    elif temperature_type not in ["K", "F", "R"]:
        return Exception("Wybierz rodzaj temp (kelvin - K, fahrenheit - F, rankine - R)")
    # calc
    if temperature_type.lower() == "F":
        temp = (temperature * 1.8) + 32
    elif temperature_type.lower() == "K":
        temp = temperature + 273.15
    elif temperature_type.lower() == "R":
        temp = (temperature + 273.15) * 1.8
    return temp


#cw5-----------------------------------------------
class Calculator:
    def add(self, x, y):
        return x + y
    def difference(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y
    
#cw6-----------------------------------------------
from z5 import Calculator

class ScienceCalculator(Calculator):
    def power(self, x, y):
        return pow(x, y)

c = ScienceCalculator()
print(c.power(5, 10))

#cw7----------------------------------------------
def function_7(text):
    return text[::-1]

text = "pomidor"
print(my_function(text))

