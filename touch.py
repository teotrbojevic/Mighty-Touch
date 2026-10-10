class LKG:
    def __init__(self, seed):
        self.u=seed
        self.a = 429493445
        self.c = 907633385
        self.m = 2**32
    def odradi(self):
        self.u=(self.u*self.a+self.c)%self.m
        return self.u/self.m
class Elem:
    def __init__(self, data):
        self.podatak=data
        self.sledeci=None
class KruznaLista:
    def __init__(self):
        self.zagl=Elem(None)
        self.zagl.sledeci=self.zagl
        self.br_elem=0
    def dodaj_na_pocetak(lista, element):
        element.sledeci=lista.zagl.sledeci
        lista.zagl.sledeci=element
        lista.br_elem+=1
    def dodaj_na_kraj(lista, element):
        tren=lista.zagl
        while tren.sledeci!=lista.zagl:
            tren=tren.sledeci
        tren.sledeci=element
        element.sledeci=lista.zagl
        lista.br_elem+=1
    def ukloni_sa_pocetka(lista):
        if (lista.zagl.sledeci!=lista.zagl):
            tren=lista.zagl.sledeci
            lista.zagl.sledeci=tren.sledeci
            izbrisani=tren.podatak
            del tren
            lista.br_elem-=1
            return izbrisani
        else:
            return 0
    def ukloni_sa_kraja(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren=lista.zagl
            while tren.sledeci!=lista.zagl:
                pret=tren
                tren=tren.sledeci
            pret.sledeci=lista.zagl
            izbrisani=tren.podatak
            del tren
            lista.br_elem-=1
            return izbrisani
        else:
            return 0
    def pogledaj_pocetak(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren=lista.zagl.sledeci
            return tren.podatak
        else:
            return 0
    def pogledaj_kraj(lista):
        if lista.zagl.sledeci!=lista.zagl:
            tren = lista.zagl
            while tren.sledeci != lista.zagl:
                tren = tren.sledeci
            return tren.podatak
        else:
            return 0
    def je_prazna(lista):
        if lista.zagl.sledeci==lista.zagl:
            return True
        else:
            return False
    def velicina(lista):
        return lista.br_elem
class Stek:
    def __init__(self):
        self.kula=KruznaLista()
    def push(lista, element):
        lista.kula.dodaj_na_kraj(element)
    def pop(lista):
        if lista.kula.velicina()!=0:
            return lista.kula.ukloni_sa_kraja()
        else:
            return 0
    def pogledaj_vrh_steka(lista):
        if lista.kula.velicina()!=0:
            return lista.kula.pogledaj_kraj()
        else:
            return 0
    def je_prazan(lista):
        return lista.kula.je_prazna()

zat_1=KruznaLista()
zat_2=KruznaLista()
otv_1=Stek()
otv_2=Stek()
postolje=KruznaLista()
poc_kar=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
prosli=0
trenutni_1=0
trenutni_2=0
nova_partija=0
naziv_vrednosti = {1: " A", 11: " J", 12: " Q", 13: " K"}
print("""===== КАРТАШКА ИГРА ===== 
1. Промешај шпил и подели карте 
2. Потез играча 1 
3. Потез играча 2 
4. Прикажи тренутно стање 
0. Излаз""")
ulaz=int(input())
while ulaz!=1 and ulaz!=0:
    if ulaz == 4:
        print("0 nema nema nema nema nema 0")
    else:
        print("\rNije odgovarajuce uneto")
    ulaz=int(input())
while ulaz!=0:
    if ulaz==1:
        zat_1 = KruznaLista()
        zat_2 = KruznaLista()
        otv_1 = Stek()
        otv_2 = Stek()
        prosli=0
        postolje = KruznaLista()
        seme=float(input())
        gen = LKG(seme)
        for i in range(51, -1, -1):
            j = 53
            while j >= 52:
                j = 0
                for s in range(8):
                    t = gen.odradi()
                    if t > 0.5:
                        j = j * 2 + 1
                    else:
                        j = j * 2
            poc_kar[i], poc_kar[j] = poc_kar[j], poc_kar[i]
            j = 0
        for i in range(52):
            poc_kar[i]=poc_kar[i]%13+1
        for i in range(26):
            zat_1.dodaj_na_pocetak(Elem(poc_kar[i]))
            zat_2.dodaj_na_pocetak(Elem(poc_kar[i+26]))
    if ulaz==2:
        if prosli==1:
            print("Vec si igrao")
        else:
            prosli=1
            nared = 3
            pret = 0
            while nared != 5:
                print("""===== ПОТЕЗ ИГРАЧА 1 ===== 
                1. Вуци карту са затвореног шпила 
                2. Вуци карту са отвореног шпила 
                3. Постави извучену карту на средину 
                4. Постави извучену карту код противника 
                5. Постави карту на своју гомилу и заврши потез 
                6. Прикажи тренутно стање""")
                nared = int(input())
                if nared < 1 or nared > 6:
                    print("Unesi ispravan broj")
                if nared == 1:
                    if pret != 1 and pret != 2:
                        if zat_1.je_prazna():
                            while not otv_1.je_prazan():
                                trenutni_1 = otv_1.pop()
                                zat_1.dodaj_na_pocetak(Elem(trenutni_1))
                            trenutni_1 = zat_1.ukloni_sa_pocetka()
                            pret = 1
                        else:
                            trenutni_1 = zat_1.ukloni_sa_pocetka()
                            pret = 1
                    else:
                        print("Vec se vuklo")
                if nared == 2:
                    if pret != 1 and pret != 2:
                        if otv_1.je_prazan():
                            print("Nema sta da se vuce")
                        else:
                            trenutni_1 = otv_1.pogledaj_vrh_steka()
                            pret = 2
                    else:
                        print("Vec se vuklo")
                if nared == 3:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se povuce karta")
                    if pret == 1:
                        if postolje.je_prazna():
                            if trenutni_1==1:
                                postolje.dodaj_na_kraj(Elem(trenutni_1))
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                        else:
                            if postolje.pogledaj_kraj()+1==trenutni_1 or postolje.pogledaj_kraj()-12==trenutni_1:
                                postolje.dodaj_na_kraj(Elem(trenutni_1))
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                    if pret == 2:
                        if postolje.je_prazna():
                            if trenutni_1==1:
                                postolje.dodaj_na_kraj(Elem(trenutni_1))
                                nebitno=otv_1.pop()
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                        else:
                            if postolje.pogledaj_kraj()+1==trenutni_1 or postolje.pogledaj_kraj()-12==trenutni_1:
                                postolje.dodaj_na_kraj(Elem(trenutni_1))
                                nebitno = otv_1.pop()
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                if nared == 4:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se povuce karta")
                    if pret == 1:
                        if otv_2.je_prazan():
                            print("Nema na sta da se stavi")
                        else:
                            if otv_2.pogledaj_vrh_steka()+1==trenutni_1 or otv_2.pogledaj_vrh_steka()-12==trenutni_1:
                                otv_2.push(Elem(trenutni_1))
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                    if pret == 2:
                        if otv_2.je_prazan():
                            print("Nema na sta da se stavi")
                        else:
                            if otv_2.pogledaj_vrh_steka()+1==trenutni_1 or otv_2.pogledaj_vrh_steka()-12==trenutni_1:
                                otv_2.push(Elem(trenutni_1))
                                nebitno = otv_1.pop()
                                pret=0
                                trenutni_1=0
                            else:
                                print("Ne moze")
                if nared == 5:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se vuce")
                        nared=3
                    if pret == 1:
                        otv_1.push(Elem(trenutni_1))
                        trenutni_1=0
                    if pret ==2:
                        nared = 0
                        pret=0
                        trenutni_1=0
                if nared == 6:
                    if trenutni_1==0:
                        br_zat1=zat_1.velicina()
                        if otv_1.je_prazan():
                            otv1_posl="nema"
                        else:
                            otv1_posl = otv_1.pogledaj_vrh_steka()
                        if otv_2.je_prazan():
                            otv2_posl="nema"
                        else:
                            otv2_posl = otv_2.pogledaj_vrh_steka()
                        if postolje.je_prazna():
                            posl="nema"
                        else:
                            posl=postolje.pogledaj_kraj()
                        br_zat2=zat_2.velicina()
                        if otv1_posl in naziv_vrednosti:
                            otv1_posl=naziv_vrednosti[otv1_posl]
                        if otv2_posl in naziv_vrednosti:
                            otv2_posl=naziv_vrednosti[otv2_posl]
                        if posl in naziv_vrednosti:
                            posl=naziv_vrednosti[posl]
                        print("{} nema {} {} {} nema {}".format(br_zat1, otv1_posl, posl, otv2_posl, br_zat2))
                    else:
                        br_zat1 = zat_1.velicina()
                        if otv_1.je_prazan():
                            otv1_posl = "nema"
                        else:
                            otv1_posl = otv_1.pogledaj_vrh_steka()
                        if otv_2.je_prazan():
                            otv2_posl = "nema"
                        else:
                            otv2_posl = otv_2.pogledaj_vrh_steka()
                        if postolje.je_prazna():
                            posl = "nema"
                        else:
                            posl = postolje.pogledaj_kraj()
                        br_zat2 = zat_2.velicina()
                        if otv1_posl in naziv_vrednosti:
                            otv1_posl = naziv_vrednosti[otv1_posl]
                        if otv2_posl in naziv_vrednosti:
                            otv2_posl = naziv_vrednosti[otv2_posl]
                        if posl in naziv_vrednosti:
                            posl = naziv_vrednosti[posl]
                        pisanje_1=trenutni_1
                        if trenutni_1 in naziv_vrednosti:
                            pisanje_1=naziv_vrednosti[trenutni_1]

                        print("{} {} {} {} {} nema {}".format(br_zat1, pisanje_1, otv1_posl, posl, otv2_posl, br_zat2))
                if otv_1.je_prazan() and zat_1.je_prazna() and trenutni_1==0:
                    print("Pobedio je igrac 1")
                    nova_partija = 0
                    nared=5
                    while nova_partija != 1:
                        print("Mora da se mesa spil")
                        nova_partija = int(input())
    if ulaz == 3:
        if prosli == 2:
            print("Vec si igrao")
        else:
            prosli=2
            nared = 3
            pret = 0
            while nared != 5:
                print("""===== ПОТЕЗ ИГРАЧА 2 ===== 
                1. Вуци карту са затвореног шпила 
                2. Вуци карту са отвореног шпила 
                3. Постави извучену карту на средину 
                4. Постави извучену карту код противника 
                5. Постави карту на своју гомилу и заврши потез 
                6. Прикажи тренутно стање""")
                nared = int(input())
                if nared < 1 or nared > 6:
                    print("Unesi ispravan broj")
                if nared == 1:
                    if pret != 1 and pret != 2:
                        if zat_2.je_prazna():
                            while not otv_2.je_prazan():
                                trenutni_2 = otv_2.pop()
                                zat_2.dodaj_na_pocetak(Elem(trenutni_2))
                            trenutni_2 = zat_2.ukloni_sa_pocetka()
                            pret = 1
                        else:
                            trenutni_2 = zat_2.ukloni_sa_pocetka()
                            pret = 1
                    else:
                        print("Vec se vuklo")
                if nared == 2:
                    if pret != 1 and pret != 2:
                        if otv_2.je_prazan():
                            print("Nema sta da se vuce")
                        else:
                            trenutni_2 = otv_2.pogledaj_vrh_steka()
                            pret = 2
                    else:
                        print("Vec se vuklo")
                if nared == 3:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se povuce karta")
                    if pret == 1:
                        if postolje.je_prazna():
                            if trenutni_2 == 1:
                                postolje.dodaj_na_kraj(Elem(trenutni_2))
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                        else:
                            if postolje.pogledaj_kraj() + 1 == trenutni_2 or postolje.pogledaj_kraj() - 12 == trenutni_2:
                                postolje.dodaj_na_kraj(Elem(trenutni_2))
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                    if pret == 2:
                        if postolje.je_prazna():
                            if trenutni_2 == 1:
                                postolje.dodaj_na_kraj(Elem(trenutni_2))
                                nebitno = otv_2.pop()
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                        else:
                            if postolje.pogledaj_kraj() + 1 == trenutni_2 or postolje.pogledaj_kraj() - 12 == trenutni_2:
                                postolje.dodaj_na_kraj(Elem(trenutni_2))
                                nebitno = otv_2.pop()
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                if nared == 4:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se povuce karta")
                    if pret == 1:
                        if otv_1.je_prazan():
                            print("Nema na sta da se stavi")
                        else:
                            if otv_1.pogledaj_vrh_steka() + 1 == trenutni_2 or otv_1.pogledaj_vrh_steka() - 12 == trenutni_2:
                                otv_1.push(Elem(trenutni_2))
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                    if pret == 2:
                        if otv_1.je_prazan():
                            print("Nema na sta da se stavi")
                        else:
                            if otv_1.pogledaj_vrh_steka() + 1 == trenutni_2 or otv_1.pogledaj_vrh_steka() - 12 == trenutni_2:
                                otv_1.push(Elem(trenutni_2))
                                nebitno = otv_2.pop()
                                pret = 0
                                trenutni_2 = 0
                            else:
                                print("Ne moze")
                if nared == 5:
                    if pret!=1 and pret!=2:
                        print("Mora prvo da se vuce")
                        nared=3
                    if pret == 1:
                        otv_2.push(Elem(trenutni_2))
                        trenutni_2 = 0
                    if pret == 2:
                        nared = 0
                        pret = 0
                        trenutni_2 = 0
                if nared == 6:
                    if trenutni_2 == 0:
                        br_zat1 = zat_1.velicina()
                        if otv_1.je_prazan():
                            otv1_posl = "nema"
                        else:
                            otv1_posl = otv_1.pogledaj_vrh_steka()
                        if otv_2.je_prazan():
                            otv2_posl = "nema"
                        else:
                            otv2_posl = otv_2.pogledaj_vrh_steka()
                        if postolje.je_prazna():
                            posl = "nema"
                        else:
                            posl = postolje.pogledaj_kraj()
                        br_zat2 = zat_2.velicina()
                        if otv1_posl in naziv_vrednosti:
                            otv1_posl = naziv_vrednosti[otv1_posl]
                        if otv2_posl in naziv_vrednosti:
                            otv2_posl = naziv_vrednosti[otv2_posl]
                        if posl in naziv_vrednosti:
                            posl = naziv_vrednosti[posl]
                        print("{} nema {} {} {} nema {}".format(br_zat1, otv1_posl, posl, otv2_posl, br_zat2))
                    else:
                        br_zat1 = zat_1.velicina()
                        if otv_1.je_prazan():
                            otv1_posl = "nema"
                        else:
                            otv1_posl = otv_1.pogledaj_vrh_steka()
                        if otv_2.je_prazan():
                            otv2_posl = "nema"
                        else:
                            otv2_posl = otv_2.pogledaj_vrh_steka()
                        if postolje.je_prazna():
                            posl = "nema"
                        else:
                            posl = postolje.pogledaj_kraj()
                        br_zat2 = zat_2.velicina()
                        if otv1_posl in naziv_vrednosti:
                            otv1_posl = naziv_vrednosti[otv1_posl]
                        if otv2_posl in naziv_vrednosti:
                            otv2_posl = naziv_vrednosti[otv2_posl]
                        if posl in naziv_vrednosti:
                            posl = naziv_vrednosti[posl]
                        pisanje_2 = trenutni_2
                        if trenutni_2 in naziv_vrednosti:
                            pisanje_2 = naziv_vrednosti[trenutni_2]

                        print("{} nema {} {} {} {} {}".format(br_zat1, otv1_posl, posl, otv2_posl, pisanje_2, br_zat2))
                if otv_2.je_prazan() and zat_2.je_prazna() and trenutni_2 ==0:
                    print("Pobedio je igrac 2")
                    nova_partija = 0
                    nared=5
                    while nova_partija != 1:
                        print("Mora da se mesa spil")
                        nova_partija = int(input())

    if ulaz == 4:
        br_zat1 = zat_1.velicina()
        if otv_1.je_prazan():
            otv1_posl = "nema"
        else:
            otv1_posl = otv_1.pogledaj_vrh_steka()
        if otv_2.je_prazan():
            otv2_posl = "nema"
        else:
            otv2_posl = otv_2.pogledaj_vrh_steka()
        if postolje.je_prazna():
            posl = "nema"
        else:
            posl = postolje.pogledaj_kraj()
        br_zat2 = zat_2.velicina()
        if otv1_posl in naziv_vrednosti:
            otv1_posl = naziv_vrednosti[otv1_posl]
        if otv2_posl in naziv_vrednosti:
            otv2_posl = naziv_vrednosti[otv2_posl]
        if posl in naziv_vrednosti:
            posl = naziv_vrednosti[posl]
        print("{} nema {} {} {} nema {}".format(br_zat1, otv1_posl, posl, otv2_posl, br_zat2))
    if ulaz > 4 or ulaz < 0:
        print("Nije unet dobar broj")
    if nova_partija!=1:
        print("""===== КАРТАШКА ИГРА ===== 
            1. Промешај шпил и подели карте 
            2. Потез играча 1 
            3. Потез играча 2 
            4. Прикажи тренутно стање 
            0. Излаз""")
        ulaz = int(input())
    if nova_partija==1:
        ulaz =nova_partija
        nova_partija=0
        prosli=0


print("Hvala sto ste igrali")













