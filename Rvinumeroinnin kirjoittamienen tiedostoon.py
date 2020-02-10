def main():
    try:
        nimi = input("Syötä tiedoston nimi: ")
        tiedosto = open(nimi, "w")
        print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
        rivi = "dummy"
        lista = []
        i = 1
        while rivi != "":
            rivi = input("")
            if rivi != "":
                i = str(i)
                kirjoitukseen = i+" "+rivi
                lista.append(rivi)
                tiedosto.write(kirjoitukseen+"\n")
                i = int(i)
                i += 1
        print("Tiedosto", nimi, "kirjoitettu.")
    except OSError:
        print("Tiedoston", nimi, "kirjoittaminen epäonnistui.")
main()