from Gep import Gep


def helyzet_elso():
    lista = []
    fajl = open("gep.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista = fajl.readlines()
    fajl.close()

    for i in range(0, len(nyers_lista), 1):
        sor_lista = nyers_lista[i].strip()
        vegso_lista = sor_lista.split("!")
        adatsor = Gep(
            vegso_lista[0],
            vegso_lista[1],
            vegso_lista[2],
            vegso_lista[3],
        )
        lista.append(adatsor)
    return lista


def gepek_szama(lista):
    gep_szamlalo = 0
    for i in range(0, len(lista), 1):
        gep_szamlalo += 1
    return gep_szamlalo


def atlag(lista):
    paros_szamolo = 0
    id_osszeg = 0
    for i in range(0, len(lista), 1):
        terem = lista[i].hely.strip("T")

        if int(terem) % 2 == 0:
            id_osszeg += int(lista[i].id)
            paros_szamolo += 1

    return id_osszeg / paros_szamolo


def legkisebb(lista):
    min = 100
    legkisebb_index = 0
    for i in range(0, len(lista), 1):
        if lista[i].tipus == "asztali":
            if int(lista[i].id) < min:
                min = int(lista[i].id)
                legkisebb_index = i

    return legkisebb_index
