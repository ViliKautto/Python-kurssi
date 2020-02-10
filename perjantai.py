def main():
    i = 5
    paiva = 1
    kuukausi = 1
    while kuukausi != 13 and paiva != 0:
        if i == 7:
            print(paiva, ".", kuukausi, ".", sep="")
            i = 0
        if paiva == 31:
            kuukausi += 1
            paiva = 0
        elif paiva == 28 and kuukausi == 2:
            kuukausi += 1
            paiva = 0
        elif kuukausi == 4 and paiva == 30:
            kuukausi += 1
            paiva = 0
        elif kuukausi == 6 and paiva == 30:
            kuukausi += 1
            paiva = 0
        elif kuukausi == 9 and paiva == 30:
            kuukausi += 1
            paiva = 0
        elif kuukausi == 11 and paiva == 30:
            kuukausi += 1
            paiva = 0
        paiva += 1
        i = i + 1



main()