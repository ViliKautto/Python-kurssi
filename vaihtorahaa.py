def main():

    rivi = input("Ostosten hinta: ")
    hinta = int(rivi)
    rivi = input("Maksettu rahasumma: ")
    maksettu = int(rivi)
    erotus = maksettu - hinta
    kymppi = erotus // 10
    jaannoseurot = erotus % 10
    vitoset = jaannoseurot // 5
    jaannoseurot = jaannoseurot % 5
    kakkoset = jaannoseurot // 2
    jaannoseurot = jaannoseurot % 2
    eurot = jaannoseurot
    if erotus == 0:
        print("Ei vaihtorahaa")
    else:
        print("Anna vaihtorahaa:")
        if kymppi == 0:
            pass
        else:
            print(kymppi, "kymppiä")
        if vitoset == 0:
            pass
        else:
            print(vitoset, "vitosta")
        if kakkoset == 0:
            pass
        else:
            print(kakkoset, "kaksieuroista")
        if eurot == 0:
            pass
        else:
            print(eurot, "euroa")

main()
