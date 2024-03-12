#!/usr/bin/env python3
import random #import ranodm modules preinsal v pythonu

hadane_cislo=input("zadej cislo: ")

if hadane_cislo.isdigit():     #overeni zda je to cislo
    hadane_cislo=int(hadane_cislo)  #prepsani cisla ze str --> na int

    if hadane_cislo<=0:
        print("zadej vetsi cislo jak 0!!")
        quit()
else:
    print("zadej cislo priste!")
    quit()

nahodny_cislo=random.randrange(hadane_cislo) #v zavrce je (start,stop) pozice, pokud chceme aby to zacinalo od nuly staci do zavory napsatt pouce to cislo doktereho chceme aby tp bylo +1 v tomto pripade je to 10
hadani=0

while True:
    hadani+=1
    cislo_uzivatele=input("hadej: ")
    if cislo_uzivatele.isdigit():    
        cislo_uzivatele=int(cislo_uzivatele)   
    else:
        print("zadej cislo priste!")
        continue
    
    if cislo_uzivatele==hadane_cislo:
        print(" uhod jsi to na ",hadani,"."," pokus")
        break
    elif cislo_uzivatele>hadane_cislo:
            print("jsi moc vysoko")
    else:
            print("jsi moc nizko")

    


