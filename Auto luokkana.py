# TIE-02100 Johdatus ohjelmointiin
# Tehtävä auto_luokkana, ohjelmakoodipohja

from math import sqrt

VALIKKOTEKSTI = "1) Tankkaa 2) Aja 3) Lopeta \n-> "
TILANNETEKSTI = "Auton tankissa on {:.1f} litraa polttoainetta ja matkamittarissa {:.1f} kilometriä."


class Auto:

    def __init__(self, tankin_koko, kulutus_satasella):
        self.__tankin_koko = tankin_koko
        self.__kulutus_satasella = kulutus_satasella
        self.__bensaa = 0
        self.__matkaa_mittarissa = 0

    def tulostaTilanne(self):
        print(TILANNETEKSTI.format(self.__bensaa,self.__matkaa_mittarissa))

    def tankkaa(self,tankataan):
        self.__tankataan = tankataan
        if self.__tankataan < 0:
           print("Bensaa ei voi ottaa pois tankista.")
        elif self.__tankin_koko >= self.__bensaa + self.__tankataan:
            self.__bensaa = self.__bensaa + self.__tankataan
        elif self.__tankin_koko < self.__bensaa + self.__tankataan:
            self.__bensaa = self.__tankin_koko

    def aja(self,matka):
        self.__matka = matka
        if matka <= 100 * self.__bensaa / self.__kulutus_satasella:
            self.__bensaa -= self.__matka * self.__kulutus_satasella/100
            self.__matkaa_mittarissa += self.__matka
        elif matka > 100 * self.__bensaa / self.__kulutus_satasella:
            self.__matkaa_mittarissa += 100 * self.__bensaa / self.__kulutus_satasella
            self.__bensaa = 0

def main():
    tankin_koko = lue_luku("Kuinka iso bensatankki ajoneuvossa on? ")
    kulutus_satasella = lue_luku("Montako litraa bensaa ajoneuvo kuluttaa "
                                 + "sadalla kilometrillä? ")

    # Tässä määritellään muuttuja auto, joka on luokan Auto olio. Tämä on
    # siis se kohta, jossa luokan Auto rakentajaa (__init__) kutsutaan!
    auto = Auto(tankin_koko, kulutus_satasella)


    while True:
        auto.tulostaTilanne()
        valinta = input(VALIKKOTEKSTI)
        if valinta == "1":
            tankataan = lue_luku("Montako litraa tankataan: ")
            auto.tankkaa(tankataan)
        elif valinta == "2":
            matka = lue_luku("Montako kilometriä ajetaan: ")
            auto.aja(matka)
        elif valinta == "3":
            break
    print("Kiitos ja hei!")


def lue_luku(kehote, virheilmoitus="Vaarantyyppinen syote!"):
    try:
        return float(input(kehote))
    except ValueError as e:
        print(virheilmoitus)
        return lue_luku(kehote, virheilmoitus)


main()
