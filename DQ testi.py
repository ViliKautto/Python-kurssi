def lue_tiedosto(tiedoston_nimi):
    """Lukee tiedostosta pelaajien pelaamat biisit ja saadut tulokset."""
    try:
        tiedosto = open(tiedoston_nimi, "r")
        p = 0
        dict = {}
        pelaajalista = []
        # Käydään tiedosto riveittäin läpi, rivi sisältää pelaajan tiedot
        for rivi in tiedosto:
            osat = rivi.strip().split(";")
            pelaaja = osat[0]  # sisältää pelaajan nimen
            pelaajalista.append(pelaaja)
            biisit = osat[1:]  # jokainen listan alkio sisältää yhden biisin
            kappaledict = {}
            # TODO luo pelaajalle tietorakenne joka sisältää
            # pelaajan pelaamat kappaleet ja niiden tulokset

            # Käydään läpi pelaajan pelaamat kappaleet yksi kerrallaan
            for biisi in biisit:
                osat = biisi.split(":")
                tulokset = osat[1].split(",")
                # Sisältää kappaleen nimen
                nimi = osat[0]
                # Sisältää listan kappaleen painalluksista (int)
                tulokset = [int(luku) for luku in tulokset]
                #print(pelaaja, nimi, tulokset)
                kappalelista = []
                kappalelista.append(nimi)
                kappaledict[nimi] = tulokset
                dict[pelaaja][nimi] = tulokset
            print(dict)
                #TODO: Yhdistä tulokset kappaleen nimeen
            # TODO: Lisää kappaleet ja tulokset sisältävä tietorakenne
            # pelaajat sisältävään tietorakenteeseen.

        ##
        return pelaajalista  # TODO palauta tietorakenne

    except IOError:
        print("Virhe: tiedostoa ei saatu luettua.")
        return None


def main():

    kertoimet = [5, 4, 2, 0, -6, -12]

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    pelaajalista = lue_tiedosto(tiedoston_nimi)
    LKM = len(pelaajalista)
    print(LKM)
    print(pelaajalista)
    pelikertalista = pelaajalista.keys()
    pelikertalista = sorted(pelikertalista)
    kappalelista = [pelaajalista]
    # TODO lisää tulostus
    for i in range(LKM):   #jokainen pelaaja kerrallaan
        laululista = pelaajalista[pelikertalista[i]].keys()
        laulumäärä = len(laululista)
        print(pelaajalista[kappalelista][i])
        for n in range(laulumäärä):
            print(laululista[n])





main()
