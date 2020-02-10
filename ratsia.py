# Kurssin nimi: Johdanto ohjelmointiin
# Tehtävän nimi: Ratsia koulun nurkalla
# Vili Kautto, 266881

from statistics import median

def lue_nopeus(alinopeuslaskuri,nopeussyöte,lista,rajoitus,rikesakkolista,sakkolista, ylinopeuslista):
    """ Sijoittaa tapauskohtaisesti nopeussyötteet oikeisiin listoihin """
    nopeuserotus = nopeussyöte - rajoitus
    if nopeussyöte < 20:
        alinopeuslaskuri += 1
    elif 8 <= nopeuserotus < 20:
        rikesakkolista.append(nopeussyöte)
        lista.append(nopeussyöte)
        ylinopeuslista.append(nopeussyöte)
    elif 20 <= nopeuserotus:
        sakkolista.append(nopeussyöte)
        lista.append(nopeussyöte)
        ylinopeuslista.append(nopeussyöte)
    elif nopeussyöte >= 20:
        lista.append(nopeussyöte)
    elif nopeuserotus >= 8:
        ylinopeuslista.append(nopeussyöte)
    return alinopeuslaskuri, lista, rikesakkolista, sakkolista, ylinopeuslista

def luo_kuva(miniminopeus,maksiminopeus,lista):
    p = 0
    k = miniminopeus
    while k <= maksiminopeus:
        laskin = lista.count(k) + lista.count(k + 1) + lista.count(
            k + 2) + lista.count(k + 3) + lista.count(k + 4)
        print(k, laskin * "#")
        k += 5
    return

def luo_muuttujat(lista):
    nopeuslista = sorted(lista)
    maksiminopeus = int(max(lista))
    miniminopeus = int(min(lista))
    vaihteluväli = int(maksiminopeus - miniminopeus)
    mediaani = median(nopeuslista)
    return nopeuslista,maksiminopeus,miniminopeus,vaihteluväli,mediaani


def lue_luku(rivi):
    if rivi > 0:
        luku = rivi
    else:
        luku = False
    return luku

def main():
    rivi = int(input("Syötä mittauspaikan nopeusrajoitus: "))
    lista = []
    rikesakkolista = []
    sakkolista = []
    ylinopeuslista = []
    rajoitus = lue_luku(rivi)

    if rajoitus != False:
        print("Syötä nopeusmittauksen tulokset, lopeta tyhjällä rivillä:")
        i = True
        alinopeuslaskuri = 0
        while i == True:
            nopeussyöte = str((input()))
            if nopeussyöte == "":
                i = False
            else:
                nopeussyöte = int(nopeussyöte)
                alinopeuslaskuri,lista,rikesakkolista,sakkolista,ylinopeuslista = lue_nopeus(alinopeuslaskuri,nopeussyöte,lista,rajoitus,rikesakkolista,sakkolista, ylinopeuslista)

        if alinopeuslaskuri > 0:
            print("Poistettiin", alinopeuslaskuri ,"kpl mittaustuloksia, joiden suuruus oli alle 20 km/h")
        tuloslkm = int(len(lista))
        if tuloslkm > 0:
            nopeuslista, maksiminopeus, miniminopeus, vaihteluväli, mediaani = luo_muuttujat(lista)
            print("Vaihteluväli:",vaihteluväli)
            print("Mediaani: {:.1f}".format(mediaani))

            if len(rikesakkolista) > 0:
                print("Rikesakon ylinopeudesta olisi saanut",
                      len(rikesakkolista), "kuljettajaa")
            if len(sakkolista) > 0:
                print("Sakon ylinopeudesta olisi saanut", len(sakkolista),
                      "kuljettajaa")
            if len(ylinopeuslista) > 0:
                print("Ylinopeudet mittausjärjestyksessä:")

            n = 0
            while len(ylinopeuslista) > n:
                print(ylinopeuslista[n])
                n += 1
            print()
            print("Graafinen esitys aineistosta:")
            luo_kuva(miniminopeus,maksiminopeus,lista)

    else:
        print("Nopeusrajoituksen tulee olla positiivinen kokonaisluku.")

main()