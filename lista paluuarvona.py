def lue_luvut(LKM):
    i = 1
    syötteet = []
    print("Syötä", LKM, "kpl lukuja:")
    while LKM >= i:
        i += 1
        rivi = input()
        syötteet.append(rivi)
    return syötteet

def main():
    LKM = int(input("Kuinka monta lukua haluat käsitellä: "))
    syötteet = lue_luvut(LKM)
    luku = input("Syötä etsittävä luku: ")
    lukumäärä = syötteet.count(luku)
    if lukumäärä <= 0:
        print(luku, "ei esiinny syöttämiesi lukujen joukossa.")
    else:
        print(luku, "esiintyy syöttämiesi lukujen joukossa", lukumäärä, "kertaa.")
main()