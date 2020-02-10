from math import sqrt

def pinta_ala(sivu1, sivu2, sivu3):
    s = (sivu1 + sivu2 + sivu3) / 2
    area = sqrt(s*(s-sivu1)*(s-sivu2)*(s-sivu3))
    return area


def main():
    area = 0
    rivi = input("Syötä ensimmäinen sivun pituus: ")
    sivu1= float(rivi)
    rivi = input("Syötä toinen sivun pituus: ")
    sivu2 = float(rivi)
    rivi = input("Syötä kolmas sivun pituus: ")
    sivu3 = float(rivi)

    pinta_ala(sivu1, sivu2, sivu3)

    print("Kolmion pinta-ala on {:.1f}".format(pinta_ala(sivu1,sivu2,sivu3)))

main()
