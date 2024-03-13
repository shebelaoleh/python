import random


hrac1_vyhra=0
hrac2_vyhra=0
vyber=["kamen","nuzky","papir"]


while True:
    uzivatel=input("zadej kamen/nuzky/papir ").lower()
    if uzivatel=="e":
        break

    if uzivatel not in vyber:
        continue

    cislo=random.randrange(0,3) #kamen0,nuzky1,papir2
    
    pocitac=vyber[cislo]
    print("pocitac zvolil",pocitac+".")

    if uzivatel=="kamen" and pocitac=="nuzky":
        print("vyhral jsi!")
        hrac1_vyhra+=1
        continue
    elif uzivatel=="papir" and pocitac=="kamen":
        print("vyhral jsi!")
        hrac1_vyhra+=1
        continue
    elif uzivatel=="nuzky" and pocitac=="papir":
        print("vyhral jsi!")
        hrac1_vyhra+=1
        continue
    else:
        print("prohral jsi!")
        hrac2_vyhra+=1

    
    
print("vyhral jsi",hrac1_vyhra,"krat")
print("pocitac vyhral",hrac2_vyhra,"krat")
print("nazdar")