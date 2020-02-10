def isot_alkukirjaimet(syöte):
    oikea_syöte = str.title(syöte)
    return oikea_syöte
def main():
    syöte = input("syötä")
    oikea_syöte = isot_alkukirjaimet(syöte)
    print(oikea_syöte)
main()
