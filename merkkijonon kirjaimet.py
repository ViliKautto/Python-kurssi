def main():
    sana = str(input("Syötä sana: "))
    p = len(sana)
    i = 0
    v = 0
    while i < p:
        if sana[i] == "a" or sana[i] == "e" or sana[i] == "i" or sana[i] == "o" or sana[i] == "u" or sana[i] == "y" or sana[i] == "ä" or sana[i] == "ö":
            v += 1
        i += 1
    k = p - v
    print("Sana", sana, "sisältää",v, "vokaalia ja",k,"konsonanttia")
main()