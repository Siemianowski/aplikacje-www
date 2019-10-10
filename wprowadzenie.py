#1
tekst="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#2
imie="qweqweqwesdfgfgh"
nazwisko="sdfgsdfg"
dane=("W tekście jest { %s } liter %s oraz { %s } liter %s")

print(dane % (tekst.count(imie[2]), imie[2], tekst.count(nazwisko[2]), nazwisko[2]))

#3
a = "Lukasz jest fajny"
b = a.replace("Lukasz", "Pawel").replace("fajny", "zgrabny")
print(b)
a2 = "pawel jest wielki".upper()
print(a2)
a3 = "LUKASZ!".lower()
print(a3)
a4 = "MEtin2"
a4 = list(a4)[2:-2]
print("".join(a4))
a5 = "Pierwsza i ostatnia literA"
print(a5[0], a5[-1])

#4
zmienna_typu_string="elit"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.casefold)
#5
print(imie[::-1]);
print(nazwisko[::-1]);
#6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
new_lista = [];
new_lista = lista[5:10];
del lista[5:10];
print(lista);
print(new_lista);
#7
listaa = lista + new_lista;
listaa.insert(0, 0);
listaaa = listaa.copy();
listaaa.sort();
listaaa.reverse();
print(listaa);
print(listaaa);


#8
krotka1=(144123, 'Vesek')
krotka2=(144124, 'Cichy')
krotka3=(144125, 'Pawko')

lista_krotek=[krotka1, krotka2, krotka3]
#(nr_albumu, imie)= krotka1
print(lista_krotek)


#9
slownik=dict(lista_krotek)
print(lista_krotek)

#10
numery_tel = [123456789, 123456789, 123456789, 987654321, 987654321]
numery_tel2 = list(set(numery_tel))

print(numery_tel2)


#11
x = range(1, 11);
for n in x:
    print(n)

#12
x = range(100, 20, -5);
for n in x:
    print(n);
