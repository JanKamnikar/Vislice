STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'

ZACETEK = 'Z'

class Vislice:
    def __init__(self):
        self.igre = {}
    def prost_id_igre(self):
        if self.igre:
            return max(self.igre)+1
        else:
            return 0
    def nova_igra(self):
        igra = nova_igra()
        id = self.prost_id_igre()
        par = (igra,ZACETEK)
        self.igre[id] = par
        return id
    def ugibaj(self, id_igre, crka):
        igra, stanje =self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra,stanje)

class Igra:
    def __init__(self, geslo,): #geslo=niz crke=seznam
        self.geslo = geslo
        self.crke = []

    def napacne_crke(self):
       return [c for c in self.crke if c.upper() not in self.geslo.upper()]
    def pravilne_crke(self):
        return [c for c in self.crke if c.upper() in self.geslo.upper()]
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK    
    def zmaga(self):
        return not self.poraz() and len(self.pravilne_crke()) == len(set(self.geslo))
        #set()ti da množico, ker množica nima ponovljenih črk npr žaba pravilne crke žba, 3!=4
    def pravilni_del_gesla(self):
        return ''.join([crka if crka in self.crke else '_' for crka in self.geslo.upper()])#c self.crke dajemo samo velike crke drugače pa samo str(self.crke).upper()
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())#join ti spremeni v niz
    def ugibaj(self,crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = f.read().split() #read spremeni v niz, split pa v seznam

import random
def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)
