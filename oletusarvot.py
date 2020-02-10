def pinta_ala(pituus, leveys = None):
    if leveys == None:
        pinta_ala =(pituus ** 2)
        return pinta_ala
    else:
        ala = pituus * leveys
        return ala

def main():
    print("Neliön pinta-ala on {:.1f}".format(pinta_ala(3)))
    print("Suorakaiteen pinta-ala on {:.1f}".format(pinta_ala(4,3)))


main()
