def main():
    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "ranta": "playa"}
    print("Sanakirjan sisältö:")
    aakkostettu = sorted(suomi_espanja)
    s = ", ".join(aakkostettu)
    print(s)
    while True:
        komento = input("[S]ana/[L]isää/[P]oista/[T]ulosta/[K]äännä/[Q]uit: ")

        if komento == "S":
            sana = input("Syötä käännettävä sana: ")
            if sana in suomi_espanja:
                print(sana, "espanjaksi on", suomi_espanja[sana])
            else:
                print("Sanaa", sana, "ei löydy sanakirjasta.")

        elif komento == "L":
            suomeksi = input("Syötä lisättävä sana suomeksi: ")
            espanjaksi = input("Syötä lisättävä sana espanjaksi: ")
            suomi_espanja [suomeksi] = espanjaksi
            aakkostettu = sorted(suomi_espanja)
            s = ", ".join(aakkostettu)
            print("Sanakirjan sisältö:")
            print(s)

        elif komento == "P":
            poisto = input("Syötä poistettava sana suomeksi: ")
            if poisto not in suomi_espanja:
                print("Sanaa", poisto, "ei löydy sanakirjasta.")
            else:
                del suomi_espanja[poisto]

        elif komento == "T":
            print("")
            print("Suomi-espanja:")
            järjestetty = sorted(suomi_espanja)
            i = 0
            espanja_suomi = {}
            for alkio in järjestetty:
                espanja_suomi[suomi_espanja[järjestetty[i]]] = järjestetty[i]
                print(järjestetty[i], suomi_espanja[järjestetty[i]])
                i += 1
            print("")
            print("Espanja-suomi:")
            järjestetty_espanja_suomi = sorted(espanja_suomi)
            i = 0
            for alkio in espanja_suomi:
                print(järjestetty_espanja_suomi[i],espanja_suomi[järjestetty_espanja_suomi[i]])
                i = i +1
            print("")

        elif komento == "K":
            lause = input("Syötä käännettävä teksti suomeksi: ")
            n = lause.count(" ") + 1
            sanalista = lause.split(" ")
            i = 0
            printti = ""
            for i in range(n):
                if sanalista[i] in suomi_espanja:
                    printti = printti + suomi_espanja[sanalista[i]] + " "
                elif sanalista[i] not in suomi_espanja:
                    printti = printti + sanalista[i] + " "
            print("Teksti sanakirjan varassa käännettynä:")
            print(printti)

        elif komento == "Q":
            print("Adios!")
            return

        else:
            print("Virheellinen komento, syötä joko S, L, P, T, K tai Q!")


main()
