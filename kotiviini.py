
def main():
    pilaantumislaskuri = 0
    pilaantumissumma = 0
    tuloslaskuri = 1
    mittaustulos = int(0)
    rivi = input("Syötä mittausten lukumäärä: ")
    mittausten_lkm = int(rivi)                                              # Luodaan ketju, joka jatkuu kunnes mittaustulosten määrä on saavutettu, tai vaihtoehtoisesti kunnes viini on mennyt pilalle.
    if mittausten_lkm > 0:
        for luku in range (0, mittausten_lkm):
            kierros = str(tuloslaskuri)
            tuloste = "Syötä "+kierros+". mittaustulos: "
            mittaustulos = input(tuloste)
            mittaustulos = int(mittaustulos)
            tuloslaskuri += 1
            if 20 > mittaustulos or 25 < mittaustulos:
                pilaantumislaskuri += 1                                     # Pilaantumisen ehdot määritetään kierroksittain kasvavalla laskurilla, jonka mukaan kaksi peräkkäistä "pilaantunutta" kierrosta johtaa viinin pilaantumiseen.
                pilaantumissumma += 1                                       # Pilaantumissumma kasvaa joka kierros, jos lämpötila ei ole suotuisa. Pilaantumislaskuri toimii samalla tavalla, mutta se nollataan,
            if pilaantumislaskuri == 1 and 20 <= mittaustulos <= 25:        # mikäli heitto suotuisan käymislämpötilan ulkopuolella kestää vain yhden kierroksen.
                pilaantumislaskuri = 0
            elif pilaantumislaskuri == 2:
                print("Viinisi on pilalla.")
                return
            elif pilaantumissumma / mittausten_lkm > 0.1:                   # Vaihtoehtoisesti viini menee pilalle, jos yli 10% mittaustuloksista johtaa pilaantumissumman kasvamiseen.
                print("Viinisi on pilalla.")
                return
            elif tuloslaskuri > mittausten_lkm and pilaantumislaskuri < 2:
                print("Viinisi on hyvää.")
    else:
        print("Mittausten lukumäärän tulee olla positiivinen kokonaisluku.")
main()

