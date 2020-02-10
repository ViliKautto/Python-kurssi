from math import pi
def valikko():
    while True:

        vastaus = (input("Syötä kuvion alkukirjain, q lopettaa (n/s/y/q): "))
        if vastaus == "n":
            line = "Syötä neliön sivun pituus: "
            nsivu = float(input(line))
            mitta = tarkista(nsivu, line)
            npiiri, nala = laske_neliö(mitta)
            print("Ympärysmitta on {:.2f}".format(npiiri))
            print("Pinta-ala on {:.2f}".format(nala))

        elif vastaus == "s":
            line = "Syötä suorakaiteen sivun 1 pituus: "
            ssivu1 = float(input(line))
            mitta1 = tarkista(ssivu1, line)
            line = "Syötä suorakaiteen sivun 2 pituus: "
            ssivu2 = float(input(line))
            mitta2 = tarkista(ssivu2, line)
            spiiri, sala = laske_suorakaide(mitta1, mitta2)
            print("Ympärysmitta on {:.2f}".format(spiiri))
            print("Pinta-ala on {:.2f}".format(sala))

        elif vastaus == "y":
            line = "Syötä ympyrän säde: "
            säde = float(input(line))
            mitta = tarkista(säde, line)
            ypiiri, yala = laske_ympyrä(mitta)
            print("Ympärysmitta on {:.2f}".format(ypiiri))
            print("Pinta-ala on {:.2f}".format(yala))

        elif vastaus == "q":
            return

        else:
            print("Virheellinen syöte, yritä uudelleen!")
        print()

def laske_ympyrä(mitta):
    ypiiri = float(2 * mitta * pi)
    yala = float( pi * mitta ** 2)
    return ypiiri, yala

def tarkista(mitta, line):
    while mitta <= 0:
        mitta = float(input(line))
    return mitta

def laske_neliö(mitta):
        npiiri = 4* mitta
        nala = float(mitta * mitta)
        return npiiri, nala

def laske_suorakaide(mitta1, mitta2):
        spiiri = float(mitta1*2+mitta2*2)
        sala = float(mitta1*mitta2)
        return spiiri, sala

def main():
    valikko()
    print("Näkemiin!")


main()