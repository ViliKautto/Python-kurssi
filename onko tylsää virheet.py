def main():
    rivi = input("Vastaa K tai E: ")
    vastaus = rivi
    while vastaus != "K" and vastaus != "E" and vastaus != "k" and vastaus != "e":
        print("Virheellinen syöte.")
        vastaus= input("Yritä uudelleen: ")
    print("Vastasit", vastaus)
main()