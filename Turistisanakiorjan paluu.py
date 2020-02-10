def tulosta_nurinpäin_aakkostettuna(suomi_espanja):
    järjestetty = sorted(suomi_espanja)
    i = 0
    kolikko = sorted(suomi_espanja, key = lambda suomi_espanja: suomi_espanja)
    if kolikko != "testi":
        espanja_suomi = {}
        for alkio in järjestetty:
            espanja_suomi[suomi_espanja[järjestetty[i]]] = järjestetty[i]
            i += 1
        järjestetty_espanja_suomi = sorted(espanja_suomi)
        i = 0
        for alkio in espanja_suomi:
            print(järjestetty_espanja_suomi[i], espanja_suomi[järjestetty_espanja_suomi[i]])
            i = i + 1
        return espanja_suomi,suomi_espanja
def main():

    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "mennään": "vamos",
                     "ravintola": "restaurante", "missä": "donde",
                     "ranta": "playa"}
    tulosta_nurinpäin_aakkostettuna(suomi_espanja)
main()