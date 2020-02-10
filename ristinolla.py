def main():
    p = str('.')
    lauta = [[p,p,p], [p,p,p], [p,p,p]]
    print("".join(lauta[0]))
    print("".join(lauta[1]))
    print("".join(lauta[2]))
    vuorot = 0

    while vuorot < 9:
        if vuorot % 2 == 0:
            merkki = "X"
        else:
            merkki = "O"
        koordinaatit = input("Pelaaja " + merkki + " anna koordinaatit: ")
        try:
            x, y = koordinaatit.split(" ")
            x = int(x)
            y = int(y)
            if lauta[y][x] == ".":
                lauta[y][x] = merkki
                print("".join(lauta[0]))
                print("".join(lauta[1]))
                print("".join(lauta[2]))
                vuorot += 1
                if vuorot > 4 and lauta[0][0] != p:
                    if lauta[0][0] == lauta[0][1] == lauta[0][2]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                    elif lauta[0][0] == lauta[1][0] == lauta[2][0]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                    elif lauta[0][0] == lauta[1][1] == lauta[2][2]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                if vuorot > 4 and lauta[1][1] != p:
                    if lauta[1][1] == lauta[1][0] == lauta[1][2]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                    elif lauta[1][1] == lauta[0][1] == lauta[2][1]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                    elif lauta[2][0] == lauta[1][1] == lauta[0][2]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                if vuorot > 4 and lauta[2][2] != p:
                    if lauta[2][2] == lauta[2][1] == lauta[2][0]:
                        print("Peli loppui, voittaja on", merkki)
                        break
                    elif lauta[2][2] == lauta[1][2] == lauta[0][2]:
                        print("Peli loppui, voittaja on", merkki)
                        break
            else:
                print("Virhe: ruutuun on jo pelattu.")



        except ValueError:
            print("Virhe: syötä kaksi kokonaislukua välilyönnillä erotettuna.")
        except IndexError:
            print("Virhe: koordinaattien oltava välillä 0-2.")

    if vuorot == 9:
        print("Tasapeli!")


main()
