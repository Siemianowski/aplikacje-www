from datetime import datetime
#1
tekst="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#2
imie="qweqweqwesdfgfgh"
nazwisko="sdfgsdfg"
dane=("W tekście jest { %s } liter %s oraz { %s } liter %s")

print(dane % (tekst.count(imie[2]), imie[2], tekst.count(nazwisko[2]), nazwisko[2]))
#3
# 3.1
format1='{:^111}'.format('zip')
print(format1)
# 3.2
format2='{:.8}'.format('xylophone')
print(format2)
# 3.3
format3='{:3d}'.format(2)
print(format3)
# 3.4
format4='{:=+10d}'.format(3)
print(format4)
# 3.5
format5='{:%m/%d/%Y %H:%M}'.format(datetime.now())
print(format5)
#4
zmienna_typu_string="elit"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.casefold)
#5
print(imie[::-1]);
print(nazwisko[::-1]);
