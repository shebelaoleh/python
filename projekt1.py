#!/usr/bin/env python3

hra=input("chces si zahrat??? ")
if hra.lower()!="ano":
    quit()
else:
    print("Jdeme na to!")

skore=0

otazka=input("otakza")
if otazka.lower()=="odpoved":
    print("spravne")
    skore+=1
else:
    print("spatna odpoved!!!")

otazka=input("otaza")
if otazka.lower()=="odpoved":
    print("spravne")
    skore+=1
else:
    print("spatna odpoved!!!")

otazka=input("otaza")
if otazka.lower()=="odpoved":
    print("spravne")
    skore+=1
else:
    print("spatna odpoved!!!")


vysledek=(skore/3)*100
zaokrouhleni=round(vysledek,0)

print("")
print("mel jsi spravne "+str(skore)+" ze 3 otazek "+"coz je: "+str(zaokrouhleni)+"%")


