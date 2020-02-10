def käännä_nimi(nimi):
    if nimi == ",":
        return ""
    if "," not in nimi:
        nimi = nimi.strip()
        return nimi
    if "," in nimi:
        nimet = nimi.split(",")
        sukunimi = nimet[0]
        etunimi = nimet[1]
        etunimi = etunimi.strip()
        sukunimi = sukunimi.strip()
        kokonimi = etunimi+" "+sukunimi
        if etunimi =="":
            return sukunimi
        if sukunimi =="":
            return etunimi
        return kokonimi
