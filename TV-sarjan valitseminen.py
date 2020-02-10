
def lue_tiedosto(tiedoston_nimi):
    """Lukee ja tallentaa tiedostossa olevat sarjat ja niiden genret."""

    genrelista = []
    nimikohtaiset_genret = {}

    try:
        tiedosto = open(tiedoston_nimi, "r")

        for rivi in tiedosto:
            # Erotellaan nimi ja genret erilleen
            # nimi on merkkijono ja genret lista
            nimi, genrelitanja = rivi.rstrip().split(";")
            genret = genrelitanja.split(",")
            LKM = len(genret)
            for i in range(LKM):
                if genret[i] not in genrelista:
                    genrelista.append(genret[i])
                if genret[i] not in nimikohtaiset_genret:
                    nimikohtaiset_genret[genret[i]] = nimi
                elif genret[i] in nimikohtaiset_genret:
                    value = str(nimikohtaiset_genret[genret[i]])+", "+nimi
                    nimikohtaiset_genret[genret[i]] = value

        tiedosto.close()
        return genrelista, nimikohtaiset_genret

    except ValueError:
        print("Virhe: rivi ei ole muotoa nimi;genret.")
        return None

    except IOError:
        print("Virhe: tiedostoa ei saada luettua.")
        return None


def main():

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    genrelista, nimikohtaiset_genret = lue_tiedosto(tiedoston_nimi)
    LKM = len(genrelista)
    genrelista = sorted(genrelista)
    printti = ""
    for i in range(LKM):
        printti += genrelista[i]+", "
    printti = printti[:-2]



    print("Valittavia genrejä ovat:", printti)

    while True:
        genre = input("> ")

        if genre == "lopeta":
            return

        else:
            try:
                lista = nimikohtaiset_genret[genre].split(", ")
                lista = sorted(lista)
                LKM = len(lista)
                tuloste = ""
                for x in range(LKM):
                    tuloste += lista[x] + "\n"
                tuloste = tuloste[:-1]
                print(tuloste)
            except KeyError:
                lista = "\n"



main()
