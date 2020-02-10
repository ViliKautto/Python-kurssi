def main():
    try:
        lue = input("Syötä luettavan tiedoston nimi: ")
        kirjoita = input("Syötä kirjoitettavan tiedoston nimi: ")
        lukutiedosto = open(lue, "r")
        kirjoitustiedosto = open(kirjoita, "w")
        rivimäärä = sum(1 for line in open(lue))
    except:
        print("Virhe tiedoston lukemisessa!")
    rivi = lukutiedosto.readline()  # Dummy
    rivi = lukutiedosto.readline()
    tunti, minuutti, sekuntit_ja_data = rivi.split(":")
    sekunti = sekuntit_ja_data[0] + sekuntit_ja_data[1]
    vanha_data = sekuntit_ja_data[3:]
    vanha_aika = 3600 * float(tunti) + 60 * float(minuutti) + float(sekunti)
    i = 1
    while i < rivimäärä-1:
        rivi = lukutiedosto.readline()
        tunti, minuutti, sekuntit_ja_data = rivi.split(":")
        sekunti = sekuntit_ja_data[0] + sekuntit_ja_data[1]
        uusi_data = sekuntit_ja_data[3:]
        uusi_aika = 3600 * float(tunti) + 60 * float(minuutti) + float(sekunti)
        uuni11, uuni12, uuni13 = vanha_data.split(";")
        uuni21, uuni22, uuni23 = uusi_data.split(";")
        uunilista = {0:uuni11,1:uuni12,2:uuni13,3:uuni21,4:uuni22,5:uuni23}
        for n in uunilista:
            try:
                k, d = uunilista[n].split(",")
                uunilista[n] = float(k+"."+d)
            except ValueError:
                uunilista[n] = float(uunilista[n])
        aikaerotus = uusi_aika-vanha_aika
        deltauuni1 = uunilista[3]-uunilista[0]
        deltauuni2 = uunilista[4]-uunilista[1]
        deltauuni3 = uunilista[5]-uunilista[2]
        uuni1keskiarvo = deltauuni1/aikaerotus
        uuni2keskiarvo = deltauuni2/aikaerotus
        uuni3keskiarvo = deltauuni3/aikaerotus
        uuni1keskiarvo = "{:.1f}".format(uuni1keskiarvo)
        uuni2keskiarvo = "{:.1f}".format(uuni2keskiarvo)
        uuni3keskiarvo = "{:.1f}".format(uuni3keskiarvo)
        aikaerotus = "{:.1f}".format(float(aikaerotus))
        tuloste = (aikaerotus)+";"+str(uuni1keskiarvo)+";"+str(uuni2keskiarvo)+";"+str(uuni3keskiarvo)+"\n"
        kirjoitustiedosto.write(tuloste)
        vanha_aika = uusi_aika
        vanha_data = uusi_data
        i += 1
    lukutiedosto.close()
    kirjoitustiedosto.close()
    print("Tietojen tallennus onnistui.")