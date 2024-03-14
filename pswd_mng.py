#pip install cryptography
#neni dokonceny nefunguje cryptography
from cryptography.fernet import Fernet



hlavni_heslo=input("heslo: ")

def klice():
    klic=Fernet.generate_klic()
    with open("klic.txt","wb") as klic_soubor:
        klic_soubor.write(klic) 


klice()


def view():  
    with open("hesla.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            jmeno,heslo=data.split("/")
            print("uzivatelske jemno:",jmeno,"•","heslo:",heslo)

def add():
    jmeno=input("uzivaelse jmeno: ")
    heslo=input("heslo: ")

    with open("hesla.txt", "a") as f:
        f.write(jmeno+"/"+heslo+"\n")


while True:
    
    mod=input("pridat heslo, nebo si prohlidnout hesla(view/add) nebo zmackni e pro exit: ").lower()
    if mod=="e":
        break

    if mod=="view":
        view()
    elif mod=="add":
        add()
    else:
        print("spatna operace")
