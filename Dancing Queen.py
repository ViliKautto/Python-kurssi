def lue_tiedosto(tiedostonnimi):

    try:
        tiedosto = open(tiedostonnimi, "r")
        pelaaja_biisi = {}
        for rivi in tiedosto:
            biisi_statsit = {}
            osat = rivi.strip().split(";")
            pelaaja = osat[0]
            biisit = osat[1:]

            for biisi in biisit:
                osat = biisi.split(":")
                nimi = osat[0]
                statsit = osat[1].split(",")
                statsit = [int(luku) for luku in statsit]
                biisi_statsit[nimi] = statsit

            pelaaja_biisi[pelaaja] = biisi_statsit
        return pelaaja_biisi

    except IOError:
        print("Virhe: tiedostoa ei saatu luettua.")
        return None


def main():

    kertoimet = [5, 4, 2, 0, -6, -12]
    tiedostonnimi = input("Anna tiedoston nimi: ")
    statsit = lue_tiedosto(tiedostonnimi)
    for pelaaja in sorted(statsit):
        print(pelaaja,":", sep="")
        for biisi in sorted(statsit[pelaaja]):
            print("- ", biisi, ": ",end="",sep="")
            biisinpisteet = 0
            for i in range(len(statsit[pelaaja][biisi])):
                biisinpisteet += (kertoimet[i]*statsit[pelaaja][biisi][i])
            maksimi = sum(statsit[pelaaja][biisi])*5
            prosentit= (biisinpisteet/maksimi * 100)
            print("{:.2f}%".format(prosentit))
main()

