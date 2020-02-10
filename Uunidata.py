def main():
    try:
        lue = input("Syötä luettavan tiedoston nimi: ")
        kirjoita = input("Syötä kirjoitettavan tiedoston nimi: ")
        lukutiedosto = open(lue, "r")
        kirjoitustiedosto = open(kirjoita, "w")
        rivimäärä = sum(1 for line in open(lue))
        rivi = lukutiedosto.readline()
        kirjoitustiedosto.write(rivi+"\n".rstrip())
        n = 0
        while n < rivimäärä-1:
            rivi = lukutiedosto.readline()
            tunti, minuutti, sekuntit_ja_data = rivi.split(":")
            sekunti = sekuntit_ja_data[0] + sekuntit_ja_data[1]
            data = sekuntit_ja_data[2:]
            aika = 3600 * int(tunti) + 60 * int(minuutti) + int(sekunti)
            siirrä = str(aika) + data + "\n".rstrip()
            kirjoitustiedosto.write(siirrä)
            n += 1
        lukutiedosto.close()
        kirjoitustiedosto.close()
        print("Tietojen tallennus onnistui.")
    except:
        print("Virhe tiedoston lukemisessa!")

main()
