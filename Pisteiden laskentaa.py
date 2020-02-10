def main():
    print("Syötä kilpailijan nimi ja pistemäärä. Lopeta syöttämällä tyhjä rivi.")
    rivi = "a"
    dict = {}
    summadict = {}
    nimilista = []
    while rivi != "":
        rivi = input("")
        if rivi == "":
            break
        nimi, numero = rivi.split(" ")
        numero = str(numero)
        if nimi not in dict:
            dict[nimi] = numero
        elif nimi in dict:
            dict[nimi] += " "+numero
        numero = int(numero)
        if nimi not in summadict:
            summadict[nimi] = numero
        elif nimi in summadict:
            summadict[nimi] += numero
    print("Kilpailijoiden pistetilanne:")
    for x in sorted(dict):
        print(x, dict[x], "=", summadict[x])



main()