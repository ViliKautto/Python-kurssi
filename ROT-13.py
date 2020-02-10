def salaa(merkki):
    if merkki == merkki.lower():
        flag = 1
    else:
        flag = 0
    merkki = merkki.lower()
    SELKOMERKIT = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    SALAMERKIT = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]

    if merkki in SELKOMERKIT:
        indeksi = SELKOMERKIT.index(merkki)
        merkki = SALAMERKIT[indeksi]
        if flag == 0:
            merkki = merkki.upper()
        return merkki
    else:
        return merkki

def rivin_salaus(mjono):
    i = 0
    salattu_jono =""
    while i < len(mjono):
        merkki = mjono[i]
        merkki = salaa(merkki)
        salattu_jono = salattu_jono + merkki
        i +=1
    return salattu_jono

def lue_viesti():
    lista = []
    rivi = "."
    indeksi = 0
    while rivi != "":
        rivi = input("")
        if rivi != "":
            lista.append(rivi)
            indeksi +=1
    return lista, indeksi


def main():
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    viesti, indeksi = lue_viesti()


    print("ROT13:")
    i=0
    salattu_lista = []
    while i<indeksi:
        salattu_jono = rivin_salaus(viesti[i])
        i += 1
        print(salattu_jono)

main()

