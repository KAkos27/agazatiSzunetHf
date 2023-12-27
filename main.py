import minosites
import sorozat
import helyzet

minosites.elso_feladat()

lista = sorozat.masodik_feladat()
oszthatok = sorozat.oszthatok_szama(lista)
sorozat.konzolra_ir(oszthatok)
sorozat.fajl_ir(oszthatok)

lista = helyzet.helyzet_elso()
gepszam = helyzet.gepek_szama(lista)
print(f"A gépek száma: {gepszam}")
atlag = helyzet.atlag(lista)
print(f"A páros teremszámú termek azonosító átlaga: {atlag}")
legkisebb = helyzet.legkisebb(lista)
print(
    f"A legkisebb asztali gép azonosítója: {lista[legkisebb].id}, helye: {lista[legkisebb].hely}."
)
