def onko_suuruusjärjestyksessä(lista):
    i = 0
    k = 1
    v = 0
    while len(lista) > k:
        if lista[i] <= lista[k]:
            v += 0
        else:
            v += 1
        i += 1
        k += 1
    if v == 0:
        return True
    else:
        return False
