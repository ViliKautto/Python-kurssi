def main():
    paiva = 1
    kuukausi = 1
    while paiva != 32 and kuukausi != 13:
        print(paiva, ".",kuukausi, ".", sep="")
        paiva += 1
        if paiva == 32:
            kuukausi += 1
            paiva = 1
        elif paiva == 29 and kuukausi == 2:
            kuukausi += 1
            paiva = 1
        elif kuukausi == 4 and paiva == 31:
            kuukausi += 1
            paiva = 1
        elif kuukausi == 6 and paiva == 31:
            kuukausi += 1
            paiva = 1
        elif kuukausi == 9 and paiva == 31:
            kuukausi += 1
            paiva = 1
        elif kuukausi == 11 and paiva == 31:
            kuukausi += 1
            paiva = 1
main()