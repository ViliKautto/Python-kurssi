def main():
    rivi = input("Onko tylsää? (k/e) ")
    vastaus = rivi
    while vastaus!= "k" and vastaus != "K":
        while vastaus != "e" and vastaus != "k" and vastaus != "K" and vastaus != "E":
            print("Virheellinen syöte.")
            vastaus = input("Yritä uudelleen: ")
        while vastaus == "e" or vastaus == "E":
            vastaus = input("Onko tylsää? (k/e) ")
    print("Noh, lopetetaan sitten.")


main()

