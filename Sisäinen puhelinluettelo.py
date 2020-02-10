def lue_tiedosto(tiedostonimi):
    tiedostomuuttuja = open(tiedostonimi, "r")
    rivimäärä = sum(1 for line in open(tiedostonimi))
    n = 0
    tiedot = {}
    while n < rivimäärä - 1:            #mahd. virhe
        rivi = tiedostomuuttuja.readline()
        huone, nimi, puh = rivi.split(";")
        key = nimi
        nimi = {huone:puh}
        tiedot[nimi] = key
        n += 1
    tiedostomuuttuja.close()
    return tiedot

def main():
    tiedostonimi = input("Syötä luettavan tiedoston nimi: ")
    tiedot = lue_tiedosto(tiedostonimi)
    print(tiedot["Essi"]["huone"])

main()