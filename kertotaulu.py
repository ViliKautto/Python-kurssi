def main():
    rivi = input("Syötä luku: ")
    luku = int(rivi)
    i = 1
    tulo = i * luku
    while tulo < 100:
        tulo = i * luku
        print (i, "*", luku, "=", tulo)
        i = i + 1

main()
