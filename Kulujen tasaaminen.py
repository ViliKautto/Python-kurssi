#TIE-02100
#Kulujen tasaaminen
#Vili Kautto, 266881

def viesti(value,keskiarvo):
    """Funktio määrittää sopivan tulosteen loppuosan tilanteen mukaan."""
    if keskiarvo - 0.05 < value < keskiarvo + 0.05:
        loppuprintti = "eikä hänellä ole maksettavaa tai saatavaa."
        return loppuprintti
    elif value > keskiarvo:
        loppuprintti = "hänen pitää saada takaisin {:.2f}".format(value-keskiarvo)
        loppuprintti += "e."
        return loppuprintti
    elif value < keskiarvo:
        loppuprintti = "hänen pitää maksaa vielä {:.2f}".format(keskiarvo-value)
        loppuprintti += "e."
        return loppuprintti


def main():
    nimi = input("Anna tiedoston nimi: ")
    try:
        lukutiedosto = open(nimi, "r")
        sanakirja = {}
        for rivi in lukutiedosto:
            rivi = rivi.rstrip()          # Muotoillaan teksti kesiteltävään formaattiin.
            key, value = rivi.split(":")
            value = float(value)
            if key not in sanakirja:        #luodaan sanakirja joka sisältää tiedoston sisällön käsiteltävässä muodossa.
                sanakirja[key] = value
            elif key in sanakirja:
                sanakirja[key] += value
        lukutiedosto.close()                # Tiedoston käsittely voidaan lopettaa, kun sen tiedot on kopioitu sanakirjaan.
        summa = sum(sanakirja.values())
        keskiarvo = summa/len(sanakirja)
        print("Kokonaiskustannukset ovat: {:.2f}e".format(summa))
        aakkoslista = sorted(sanakirja)
        for i in range(len(aakkoslista)):           # Määritetään sopiva tulosteen alkuosa, loppuosa saadaan funktiosta.
            value = sanakirja[aakkoslista[i]]
            printti = "on maksanut {:.2f}e,".format((sanakirja[aakkoslista[i]]))
            loppuprintti = viesti(value, keskiarvo)
            print(aakkoslista[i], printti, loppuprintti)
    except OSError:
        print("Virhe! Tiedostoa", nimi,"ei voida lukea.")
    except ValueError:
        print("Virhe! Tiedoston rivien pitää olla muotoa nimi:summa.")
main()