def main():
    print("Anna 5 lukua: ")
    syötteet = []
    i = int(0)
    for syöte in range (0,5):
        syöte = int(input("Seuraava luku: "))
        if syöte > 0:
            syötteet.append(syöte)
            i += 1
    print("Syöttämäsi nollaa suuremmat luvut olivat:")
    for i in range (i):
        print(syötteet[i])
main()