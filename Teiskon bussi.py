def main():
    lista = [630, 1015, 1415, 1620, 1720, 2000]
    syöte = int(input("Mitä kello on nyt? (kokonaislukuna): "))
    print("Seuraavat bussivuorot lähtevät:")
    if syöte > 2000:
        syöte = 0
    i = 0
    if syöte <= 1620:
        while syöte > lista[i]:
            i += 1
        print(lista[i])
        print(lista[i+1])
        print(lista[i+2])
    elif 1620 < syöte <= 2000:
        lista = lista + [630, 1015]
        i = 4
        k = 1
        if 1720<syöte<= 2000:
            i = 5
        while k <= 3:
            print(lista[i])
            i += 1
            k += 1
main()