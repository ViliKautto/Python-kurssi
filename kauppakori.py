# TODO:
# määrittele tänne tarvitsemasi funktiot
def lue_tiedosto():
    try:
        tiedostomuuttuja = open("tuotetiedot.txt", "r")
        halvin_tuotelista = {}
        kauppalista = []
        tuote_ja_hinta = {}
        kauppakohtaiset_merkkijonot = {}
        kauppa_tuote_ja_hinta = {}
        for rivi in tiedostomuuttuja:
            rivi = rivi.split("\n")
            kauppa, tuote, hinta = rivi[0].split(":")
            if kauppa not in kauppakohtaiset_merkkijonot:
                kauppakohtaiset_merkkijonot[kauppa] = str(tuote + "," + hinta)
            elif kauppa in kauppakohtaiset_merkkijonot:
                kauppakohtaiset_merkkijonot[kauppa] += str("/"+tuote+","+hinta)
            if kauppa not in kauppalista:
                kauppalista.append(kauppa)
            if tuote not in halvin_tuotelista:
                halvin_tuotelista[tuote] = hinta
            elif halvin_tuotelista[tuote] > hinta:
                halvin_tuotelista[tuote] = hinta
            tuote_ja_hinta[tuote] = hinta
            kauppa_tuote_ja_hinta[kauppa] = tuote_ja_hinta
        kauppalista = sorted(kauppalista)
        flag = "True"
        tiedostomuuttuja.close()
        return flag, halvin_tuotelista, kauppalista, kauppa_tuote_ja_hinta,kauppakohtaiset_merkkijonot

    except FileNotFoundError:
        flag = "False"
        halvin_tuotelista = "dummy"
        kauppalista = "dummy"
        kauppa_tuote_ja_hinta = "dummy"
        return flag, halvin_tuotelista, kauppalista, kauppa_tuote_ja_hinta



def main():

    # TODO
    # Kutsu tässä tiedostonlukufunktiota. Huomaa,
    # että exitiä ei saa käyttää ohjelman suorituksen
    # lopettamiseen.
    flag, halvin_tuotelista, kauppalista, kauppa_tuote_ja_hinta,kauppakohtaiset_merkkijonot = lue_tiedosto()
    if flag == "False":
        pass
    elif flag != "False":
        print("Tervetuloa kauppakorisovellukseen!\n"
              "Käytettävissä olevat komennot:\n"
              " T ulosta kaupat tuotteineen\n"
              " S aatavilla olevien tuotteiden listaus\n"
              " K auppakorin halvin myyjä\n"
              " Q uit\n")

        syöte = ""
        while syöte != "Q":
            syöte = input("\nAnna komento (T, S, K, Q): ").upper()

            # HUOMIO!
            # pass on kätevä komento, joka tarkoittaa "älä tee mitään".
            # Nyt kun käyttöliittymässä on pass jokaisen ehtolauseen
            # jälkeen, tämän Python-tiedoston voi suorittaa ilman, että
            # Python-tulkki valittaa virheellisestä koodista. Näin on
            # kätevää ensin paneutua tiedoston lukemiseen ja sitten
            # ensimmäiseen komentoon (T). Muiden komentojen kohdalla
            # voi lukea pass niin kauan kunnes niitä aletaan tehdä,
            # jolloin pass kuuluu poistaa koodista.

            if syöte == "T":
                LKM = len(kauppalista)
                for i in range(LKM):
                    kauppa = (kauppalista[i])
                    print(kauppa)
                    tuotehinta = kauppakohtaiset_merkkijonot[kauppa].split("/")
                    valikoima = len(tuotehinta)
                    print(tuotehinta)
                    for n in range(valikoima):
                        tuotelista, hintalista = tuotehinta[n].split(",")
                        print(tuotelista,hintalista)
                        print("{:<15}{:>10.2}\n".format(tuotelista,hintalista))



                # TODO: kauppakohtainen tulostus


            elif syöte == "S":
                pass
                # TODO: saatavilla olevien tuotteiden tulostus

            elif syöte == "K":
                pass
                # TODO: kauppakori

            elif syöte == "Q":
                print("Hei hei!")
                return

            else:
                print("Virheellinen komento!")

main()
