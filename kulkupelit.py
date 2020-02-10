def järjestä_kirjainkoosta_välittämättä(kulkupelejä):
    lista = []
    lista = sorted(kulkupelejä, key = lambda kulkupelejä: kulkupelejä.lower())
    print(lista)
    return

def main():
    kulkupelejä = ["Mersu", "Bemari", "Lada", "auto", "Audi", "kaara"]
    rivi = järjestä_kirjainkoosta_välittämättä(kulkupelejä)
main()