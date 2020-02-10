def pituuden_tarkastelu(lista):
    määrä = len(lista)
    i = 0
    mjono = lista[i]
    while i < määrä:
        if len(mjono)<len(lista):
            mjono = lista[i]
        i += 1
    return mjono





def pisin_jarjestetty_alimerkkijono(sana):
    i = 1
    b = len(sana)
    mjono = ""
    lista = []
    if sana != "":
        edellinen = sana[0]
        mjono += sana[0]
        lista.append(sana[0])
    while i<b:
        if sana[i] < edellinen:
            edellinen = sana[i]
            mjono = sana[i]
            i += 1
            if i == b:
                break
        while sana[i] > edellinen:
            mjono += sana[i]
            edellinen = sana[i]
            i += 1
            if i == b:
                break
        if sana[b-1]>edellinen:
            mjono += sana[b-1]


        lista.append(mjono)
        mjono = pituuden_tarkastelu(lista)
        return mjono
def main():
    sana = input("syötä")
    alimerkkijono = pisin_jarjestetty_alimerkkijono(sana)
    print(alimerkkijono)
main()