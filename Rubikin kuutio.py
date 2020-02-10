def laske_aika(lista):
    lista.sort()
    del lista[0]
    del lista[3]
    summa = lista[0] + lista[1] + lista[2]
    keskiarvo = summa / 3
    return keskiarvo

def main():
    i = int(1)
    lista = []
    while i < 6:
        i =str(i)
        syöte = float(input("Syötä "+ i +". suorituksen aika: "))
        i =int(i)
        i += 1
        lista.append(syöte)
    aika = laske_aika(lista)
    print("Virallinen kilpailutulos on {:.2f} sekuntia.".format(aika))
main()