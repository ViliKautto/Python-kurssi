def main():
    rivi = "a"
    laskuri = {}
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    while rivi != "":
        rivi = input("")
        rivi = rivi.lower()
        if rivi == "":
            break
        sanalista = rivi.split(" ")
        i = 0
        for s in range(len(sanalista)):
            s = sanalista[i]
            if s not in laskuri:
                laskuri [s] = 1
            elif s in laskuri:
                laskuri[s] += 1
            i +=1
    for x in sorted(laskuri):
        print(x," :", laskuri[x], "kpl" )



main()