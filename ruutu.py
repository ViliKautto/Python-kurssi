def tulosta_ruutu(leveys, korkeus, merkki):
    i = 0
    n = 0
    for i in range (0,korkeus):
        for n in range(0,leveys):
            print(merkki, end="")
        print()


def main():
    rivi = input("Syötä ruudun leveys: ")
    l = int(rivi)
    rivi = input("Syötä ruudun korkeus: ")
    k = int(rivi)
    m = input("Syötä tulostusmerkki: ")
    print()

    tulosta_ruutu(l, k, m)

main()
