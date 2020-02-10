def laske_annos(paino, aika, kokonaisannos):
    päivittäisannos = 4000 - kokonaisannos
    if kokonaisannos >= 4000 or aika < 6:
        annos = 0
    elif (paino * 15) <= päivittäisannos:
        annos = paino * 15
    elif (paino * 15) > päivittäisannos:
        annos = päivittäisannos
    return annos



def main():
    paino = int(input("Potilaan paino (kg): "))
    aika = int(input("Kauanko aikaa edellisestä annoksesta (tasatunteina): "))
    kokonaisannos = int(input("Kokonaisannos viimeisen 24 tunnin aikana (mg): "))
    annos = laske_annos(paino, aika, kokonaisannos)
    print("Potilaalle voi antaa parasetamolia:", annos)
main()