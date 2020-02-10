def main():
    try:
        nimi = input("Syötä tiedoston nimi: ")
        tiedostomuuttuja = open(nimi, "r")
        n = sum(1 for line in open(nimi))
        rivi = "dummy"
        i = 1
        while i <= n:
            rivi = tiedostomuuttuja.readline()
            rivi = rivi.rstrip()
            print (i, rivi)
            i = i +1
        tiedostomuuttuja.close()
    except FileNotFoundError:
        print("Virhe tiedoston lukemisessa.")
    except PermissionError:
        print("Virhe tiedoston lukemisessa.")
    except FileExistsError:
        print("Virhe tiedoston lukemisessa.")
main()