# Täydennä tähän tiedostoon kaikki kohdat, joissa lukee TODO
# TIE-02100 Johdatus ohjelmointiin, KK2016
# TODO: 266881 vili.kautto@stundent.tut.fi
# TODO: Ohjelmointitehtävä T3, valmis koodirunko
# TODO: Saat myös halutessasi poistaa kommentteja,
# TODO: joissa selitetään tehtävänantoa.

from math import sqrt


# Tämä on tekstikäyttöliittymämme päävalikko ja siihen liittyvä
# käyttäjän syötteiden käsittely. Sinun tulee muokata vain TODO:lla merkityt
# kohdat, joissa kutsutaan sinun itsesi toteuttamia funktioita ja
# tallennetaan funktioiden palauttamat arvot sopiviin muuttujiin.
def valikko():
    tankin_koko  = lue_luku("Kuinka iso bensatankki ajoneuvossa on? ")
    bensaa = tankin_koko
    kulutus_satasella = lue_luku("Montako litraa bensaa ajoneuvo kuluttaa "
        + "sadalla kilometrillä? ")
    x = 0.0
    y = 0.0


    VALIKKOTEKSTI =  "1) Tankkaa 2) Aja 3) Lopeta \n-> "

    while True:
        print("Koordinaatit x={:.1f}, y={:.1f}, "
              "tankissa on {:.1f} litraa polttoainetta.".format(x, y, bensaa))

        valinta = input(VALIKKOTEKSTI)

        if valinta == "1":
           tankataan = lue_luku("Montako litraa tankataan: ")
           bensaa = tankkaa(tankin_koko, tankataan, bensaa)

        elif valinta == "2":
           uusi_x = lue_luku("x: ")
           uusi_y = lue_luku("y: ")
           bensaa, x, y = aja(x,y,uusi_x,uusi_y, bensaa, kulutus_satasella)

        elif valinta == "3":
           break

    print("Kiitos ja hei!")



def tankkaa(tankin_koko, tankataan, bensaa):
    if tankataan < 0 and bensaa + tankataan < 0:
        bensaa = 0
        return bensaa
    elif bensaa + tankataan <= tankin_koko:
        bensaa =float(bensaa + tankataan)
        return bensaa
    else:
        bensaa = float(tankin_koko)
        return bensaa

def aja(x,y,uusi_x,uusi_y,bensaa, kulutus_satasella):
    matka = float(laske_matka(x,y,uusi_x,uusi_y))
    bensaa, uusi_x, uusi_y = laske_kulutus(bensaa, matka, kulutus_satasella, uusi_x, uusi_y,x,y)
    x = float(uusi_x)
    y = float(uusi_y)
    return bensaa, x, y


def laske_kulutus(bensaa, matka, kulutus_satasella, uusi_x, uusi_y,x,y):
    tankilla_päästään = float(100 * bensaa / kulutus_satasella)
    delta_x = float(uusi_x - x)
    delta_y = float(uusi_y - y)
    matka_x = float(1)
    matka_y = float(1)
    flag_x = float(1)
    flag_y = float(1)
    flag_k = float(1)
    if tankilla_päästään >= matka:
        bensaa_kului = float(matka * kulutus_satasella/100)
        bensaa = float(bensaa - bensaa_kului)
        return bensaa, uusi_x, uusi_y
    elif tankilla_päästään < matka:
        matka = tankilla_päästään
        if delta_x == 0:
            matka_y = float(matka)
            matka_x = float(0)
        elif delta_x != 0:
            kulmakerroin = float(delta_y / delta_x)
            if kulmakerroin < 0:
                flag_k =float (-1)
            matka_x = float(sqrt(matka ** 2 / (kulmakerroin ** 2 + 1)))
            matka_y = float(kulmakerroin * matka_x)
        bensaa = float(0)
        flag_x, flag_y, = merkkitarkastelu(flag_x, flag_y,delta_x, delta_y)
        uusi_x = float(matka_x * flag_x+x)
        uusi_y = float(matka_y * flag_y*flag_k+y)
        return bensaa, uusi_x, uusi_y

def merkkitarkastelu(flag_x, flag_y, delta_x, delta_y,):
    if delta_x < 0:
        flag_x = float(-1)
    elif delta_y < 0:
        flag_y = float(-1)
    return flag_x,flag_y,

def laske_matka(x,y,uusi_x,uusi_y):
    matka = float(sqrt((abs(uusi_x-x))**2+(abs(uusi_y-y))**2))
    return matka


def lue_luku(kehote, virheilmoitus="Vääräntyyppinen syöte!"):
    try:
        return float(input(kehote))
    except ValueError as e:
        print(virheilmoitus)
        return lue_luku(kehote, virheilmoitus)


def main():
    valikko()


main()
