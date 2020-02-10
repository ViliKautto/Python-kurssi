def main():
    pyksi = input ("Pelaaja 1, syötä valintasi (K/P/S): ")
    pkaksi = input("Pelaaja 2, syötä valintasi (K/P/S): ")
    if pyksi == "K" and pkaksi == "K":
        print ("Tuli tasapeli.")
    elif pyksi == "P" and pkaksi == "P":
        print ("Tuli tasapeli.")
    elif pyksi == "S" and pkaksi == "S":
        print("Tuli tasapeli.")
    elif pyksi == "K" and pkaksi == "P":
        print("Pelaaja 2 voitti!")
    elif pyksi == "P" and pkaksi == "S":
        print("Pelaaja 2 voitti!")
    elif pyksi == "S" and pkaksi == "K":
        print("Pelaaja 2 voitti!")
    else:
        print("Pelaaja 1 voitti!")
main()
