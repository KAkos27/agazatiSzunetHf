def elso_feladat():
    mnev:str=str(input("Múzeum neve: "))
    lnev:str=str(input("Látogató Neve: "))
    ert:int=int(input("Értékelés (1-20): "))

    while not (0 <= ert <= 20):
        if ert < 0:
            print("Az értékelés nem lehet negatív vagy 0!")
            ert:int=int(input("Értékelés (1-20): "))
        else:
            print("20 pont feletti értékelés nem elfogadható!")
            ert:int=int(input("Értékelés (1-20): "))
    print("Köszönjük az értékelést!")
    