def tee_akronyymi(sana):
    sanat = sana.split(" ")
    pituus = len(sanat)
    kirjaimet = []
    i = 0
    while pituus > i:
        sana = sanat[i]
        kirjaimet.append(sana[0])
        i += 1
    i = 0
    akronyymi = ""
    while i < pituus:
        akronyymi = akronyymi + kirjaimet[i]
        i += 1
    akronyymi = akronyymi.upper()
    return akronyymi