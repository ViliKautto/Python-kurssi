def lue_syöte(line):
    rivi = -1
    while rivi <= 0:
        try:
            rivi = int(input(line))
        except ValueError:
            rivi = -1
    return rivi

def tulosta_ruutu(l, k, m):
    i = 0
    n = 0
    for i in range (0,k):
        for n in range(0,l):
            print(m, end="")
        print()

def main():
    l = 0
    line = "Syötä ruudun leveys: "
    l = lue_syöte(line)
    line = "Syötä ruudun korkeus: "
    k = lue_syöte(line)
    m = input("Syötä tulostusmerkki: ")
    print()
    tulosta_ruutu(l, k, m)
main()