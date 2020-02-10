def main():
    print("Anna sademaaria, lopeta luvulla 999999.")
    summa = 0
    i = -1
    syote = 0
    a = 0
    while syote != 999999:
        if syote < 0:
            a = 1
            rivi = input("Anna sademaara: ")
            syote = float(rivi)
        else:
            arvo = syote
            rivi = input("Anna sademaara: ")
            syote = float(rivi)
            summa = summa + arvo
            i = i + 1

    if i == 0:
        print("Yhtaan sademaaraa ei syotetty.")
    else:
        keskiarvo = summa / i
        vastaus = float(keskiarvo)
        print("Sademaarien keskiarvo on",vastaus)
main()