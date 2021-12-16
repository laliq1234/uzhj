import math, cmath


a= input('Kérem a elsőfokú egyenlet főegyütthatóját: ')
a= float(a)
b= input('Kérem a elsőfokú egyenlet konstansát: ')
b= float(b)
if a != 0:
    x=-b/a
    print (" A megoldás értéke: " + x )
else:
    if b == 0:
        print(" Minden valós szám megoldás ")
    else:
        print (" Nincs megoldás")
