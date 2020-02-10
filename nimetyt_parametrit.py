
def tulosta_ruutu(leveys, korkeus, reunamerkki = "#", sisämerkki = " "):
    print(leveys*reunamerkki)
    k = korkeus-2
    l = leveys-2
    for i in range(k):
        print(reunamerkki, sisämerkki*l, reunamerkki,sep="" )
    print(leveys * reunamerkki,sep="")
    print()

def main():
    tulosta_ruutu(5, 4)
    tulosta_ruutu(3, 8, "*")
    tulosta_ruutu(5, 4, "O", "o")
    tulosta_ruutu(sisämerkki=".", reunamerkki="O", korkeus=4, leveys=6)

main()
