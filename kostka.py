import random

def hod():
    min_hod=1
    max_hod=6
    hod=random.randrange(min_hod,max_hod+1)

    return hod

while True:
    hraci=input("zadej pocet hracu(1/4): ")
    if hraci.isdigit():
        hraci=int(hraci)
        if 2<=hraci<=4:
            break
        else:
            print("musi byt 2 az 4 hrace!")
    else:
        print("chyba!!!!!!!")

max_skore=100
hraci_skore=[0 for _ in range(hraci)]

while max(hraci_skore)<max_skore:

    for hraci_id in range(hraci):
        print("\nhrac",hraci_id+1,"kolo zacalo\n")
        print("tvoje momentalni skore je:",hraci_skore[hraci_id],"\n")
        momentalni_skore=0

        while True:
            otazka=input("chces hodit?: ")
            if otazka.lower()!="ano":
                break

            hodnota=hod()
            if hodnota==1:
                print("hodil jsi 1")
                break
            else:
                momentalni_skore+=hodnota
                print("hodil jsi:",hodnota)
            
            print("tvoje skore je:", momentalni_skore)
        
        hraci_skore[hraci_id]+=momentalni_skore
        print("tvoje momentalni skore je:",hraci_skore[hraci_id])

max_skore=max(hraci_skore)
vyhra_id=hraci_skore.index(max_skore)
print("hrac cislo",vyhra_id+1,"se sava vyhercem se skore:",max_skore)