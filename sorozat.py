import random
import math

def masodik_feladat():
    szam_lista_szoveg:str=""
    szam_lista:str=[]

    for i in range(0,16,1):
        szam:int = math.floor(random.random()*591-90)
        szam_lista_szoveg+=str(szam)
        if i != 15:
            szam_lista_szoveg+="*"
    
    szam_lista.append(szam_lista_szoveg)
    print(szam_lista)
    return szam_lista
    
def oszthatok_szama(lista):
    lista = lista[0].split("*")
    oszthatok:int = 0

    for i in range(0,len(lista),1):
        if int(lista[i]) % 10 == 0:
            oszthatok += 1
    return oszthatok