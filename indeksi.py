def main():
    print("Anna 5 lukua: ")
    syötteet = []
    i = int(5)
    for syöte in range (0,5):
        syöte = int(input("Seuraava luku: "))
        syötteet.append(syöte)
    print("Syöttämäsi luvut päinvastaisessa järjestyksessä:")
    for i in range (5):
        k = 5
        i = i+1
        print(syötteet[k-i])

main()