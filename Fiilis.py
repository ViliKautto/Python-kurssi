def main():
    rivi = input("Mikä fiilis? (1-10)")
    fiilis = float(rivi)
    if fiilis == 1:
        print ("Tunnelmaan sopiva hymiö voisi olla :'(")
    elif fiilis == 10:
        print("Tunnelmaan sopiva hymiö voisi olla :-D")
    elif fiilis > 10:
        print ("Virheellinen syöte!")
    elif fiilis < 1:
        print ("Virheellinen syöte!")
    elif fiilis > 1 and fiilis <4:
        print ("Tunnelmaan sopiva hymiö voisi olla :-(")
    elif fiilis < 10 and fiilis > 7:
        print ("Tunnelmaan sopiva hymiö voisi olla :-)")
    else:
        print ("Tunnelmaan sopiva hymiö voisi olla :-|")
main()
