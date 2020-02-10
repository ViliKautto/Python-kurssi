# Tämä dict on globaali vakio, jota hyödynnetään tulevaisuudessa hyökkäysten
# tehokkuuksien laskemisessa. Kyseessä on dict jonka avaimina on tyyppejä ja
# arvoina dictejä, joissa avaimina hyökkäysten tyyppejä ja arvoina niiden
# tehokkuuskertoimia. Esimerkiksi Normal-tyypin Pokemoniin Ghost-tyyppinen
# isku tekee 0.8x vahinkoa, mutta Fighting-tyyppinen 1.25-kertaisesti.
TYYPIT = {"Normal": {"Fighting": 1.25, "Ghost": 0.8},
          "Fighting": {"Flying": 1.25, "Psychic": 1.25, "Fairy": 1.25,
                       "Rock": 0.8, "Bug": 0.8, "Dark": 0.8},
          "Flying": {"Electric": 1.25, "Rock": 1.25, "Ice": 1.25, "Grass": 0.8,
                     "Bug": 0.8, "Fighting": 0.8, "Ground": 0.8},
          "Poison": {"Ground": 1.25, "Psychic": 1.25, "Fighting": 0.8,
                     "Bug": 0.8, "Poison": 0.8, "Grass": 0.8, "Fairy": 0.8},
          "Ground": {"Water": 1.25, "Grass": 1.25, "Ice": 1.25, "Poison": 0.8,
                     "Rock": 0.8, "Electric": 0.8},
          "Rock": {"Fighting": 1.25, "Ground": 1.25, "Steel": 1.25,
                   "Water": 1.25, "Grass": 1.25, "Normal": 0.8, "Flying": 0.8,
                   "Poison": 0.8, "Fire": 0.8},
          "Bug": {"Flying": 1.25, "Rock": 1.25, "Fire": 1.25, "Fighting": 0.8,
                  "Ground": 0.8, "Grass": 0.8},
          "Ghost": {"Ghost": 1.25, "Dark": 1.25, "Bug": 0.8, "Poison": 0.8,
                    "Normal": 0.8, "Fighting": 0.8},
          "Steel": {"Fighting": 1.25, "Ground": 1.25, "Fire": 1.25,
                    "Normal": 0.8, "Flying": 0.8, "Rock": 0.8, "Bug": 0.8,
                    "Steel": 0.8, "Grass": 0.8, "Psychic": 0.8, "Ice": 0.8,
                    "Dragon": 0.8, "Fairy": 0.8, "Poison": 0.8},
          "Fire": {"Ground": 1.25, "Rock": 1.25, "Water": 1.25, "Bug": 0.8,
                   "Steel": 0.8, "Fire": 0.8, "Ice": 0.8, "Fairy": 0.8},
          "Water": {"Grass": 1.25, "Electric": 1.25, "Steel": 0.8, "Fire": 0.8,
                    "Water": 0.8, "Ice": 0.8},
          "Grass": {"Flying": 1.25, "Poison": 1.25, "Bug": 1.25, "Fire": 1.25,
                    "Ice": 1.25, "Ground": 0.8, "Water": 0.8, "Grass": 0.8,
                    "Electric": 0.8},
          "Electric": {"Ground": 1.25, "Flying": 0.8, "Steel": 0.8,
                       "Electric": 0.8},
          "Psychic": {"Bug": 1.25, "Ghost": 1.25, "Dark": 1.25, "Fighting": 0.8,
                      "Psychic": 0.8},
          "Ice": {"Fighting": 1.25, "Rock": 1.25, "Steel": 1.25, "Fire": 1.25,
                  "Ice": 1.25},
          "Dragon": {"Ice": 1.25, "Dragon": 1.25, "Fairy": 1.25, "Fire": 0.8,
                     "Grass": 0.8, "Water": 0.8, "Electric": 0.8},
          "Dark": {"Fighting": 1.25, "Bug": 1.25, "Fairy": 1.25, "Ghost": 0.8,
                   "Psychic": 0.8},
          "Fairy": {"Poison": 1.25, "Steel": 1.25, "Fighting": 0.8, "Bug": 0.8,
                    "Dark": 0.8, "Dragon": 0.8}}


def hae_kerroin(hyökkäyksen_tyyppi, pokemonin_tyyppi):
    """
    Etsii tietorakenteesta tiedon siitä kuinka paljon vahinkoa
    tietyn tyyppinen hyökkäys tekee Pokemonille.
    :param hyökkäyksen_tyyppi: Merkkijono
    :param pokemonin_tyyppi:   Merkkijono
    :return: Palauttaa kertoimen vahingon määrälle.
    """
    if pokemonin_tyyppi in TYYPIT:

        if hyökkäyksen_tyyppi in TYYPIT[pokemonin_tyyppi]:
            return TYYPIT[pokemonin_tyyppi][hyökkäyksen_tyyppi]

    return 1

class Pokemon:
    """ Kuvaa yhtä Pokemonia, joka koostuu nimestä, tyypeistä, osumapisteistä,
        tasosta ja liikkeistä."""

    def __init__(self, laji, tyypit, hp=50, level=20):
        """
        Luokan rakentaja. Tarkastaa että kesto ja taso ovat järkeviä, ja
        tallentaa tiedot.

        :param laji:   Pokemonin laji
        :param tyypit: Pokemonin tyypit
        :param hp:     Pokemonin kestopisteiden määrä
        :param level:  Millä tasolla Pokemon on
        """
        self.__dict = []
        self.__liikelista = []
        self.__laji = laji.capitalize()
        self.__tyypit = tyypit

        if not isinstance(hp, int) or not isinstance(level, int) \
                or hp < 0 or level < 1:
            raise ValueError

        self.__hp = hp
        self.__max_hp = hp
        self.__level = level
        self.__liikkeet = {}
        self.__fainted = False

    def aseta_tyypit(self, tyyppilista):
        n = 0
        for i in range(len(tyyppilista)):
            rivi = tyyppilista[i]
            rivi = rivi.title()
            if rivi.title() in TYYPIT and rivi.title() not in self.__tyypit:
                n += 1
        if len(tyyppilista) == n:
            self.__tyypit = []
            for i in range(len(tyyppilista)):
                mjono = tyyppilista[i]
                mjono = mjono.title()
                self.__tyypit.append(mjono)
            return True
        elif len(tyyppilista) != n:
            return False

    def lisää_tyyppi(self, rivi):
        rivi = rivi.title()
        if rivi.title() in TYYPIT and rivi.title() not in self.__tyypit:
            self.__tyypit.append(rivi.title())
            return True
        else:
            return False

    def lisää_liike(self, liike, voima, tyyppi):
        liike = liike.lower()
        liike = liike.title()
        if liike == str(liike) and len(self.__liikkeet) < 2:
            self.__liikkeet[liike] = "{}, {}".format(voima, tyyppi.title())
            return True
        else:
            return False

    def tulosta_liikkeet(self):
        print("{}'s moves:".format(self.__laji.title()))
        for muuvi in sorted(self.__liikkeet):
            print("{}, {}".format(muuvi, self.__liikkeet[muuvi]))
        print()


    def tulosta(self):
        """
        Tulostaa Pokemonin muodossa laji, tyypit, jäljellä olevat osumapisteet.
        """
        print(self.__laji, ", ", self.__hp, "hp", ", Types: ",
              ", ".join(self.__tyypit), sep="")
        print()

    def paranna(self, parannus):
        try:
            parannus = int(parannus)
            if parannus > 0:
                if self.__hp + parannus <= self.__max_hp:
                    self.__hp = self.__hp + parannus
                    print(self.__laji, "was healed for", parannus, "hp.")
                elif self.__hp + parannus > self.__max_hp:
                    print(self.__laji, "was healed for", self.__max_hp - self.__hp,"hp")
                    self.__hp = self.__max_hp
                return True
            else:
                return False
        except ValueError:
            return False


        except ValueError:
            return False

    def hyökkää(self, liike, kohde):
        try:
            if self.__fainted is False:
                self.__liike = liike.title()
                self.__kohde = kohde
                self.__liike = self.__liikkeet[self.__liike]
                self.__liike = self.__liike.title()
                self.__lämä, self.__hyökkäystyyppi = self.__liike.split(", ")
                self.__lämä = float(self.__lämä)
                self.__kerroin = 1.00
                for i in range(len(kohde._Pokemon__tyypit)):
                    self.__puolustustyyppi = kohde._Pokemon__tyypit[i]
                    self.__kerroin *= float(hae_kerroin(self.__hyökkäystyyppi, self.__puolustustyyppi))
                self.__lämä *= float(self.__kerroin)
                print("{} used {}.".format(self.__laji, liike.title()))
                if int(self.__kerroin) < 1.00:
                    print("It's not very effective.")
                if int(self.__kerroin) > 1.00:
                    print("It's super effective!")
                self.__kohde.vahingoita(self.__lämä)
                print("")
                if self.__fainted is False:
                    return True
            else:
                print("Pokemon has fainted and can't attack.")
                return False
        except KeyError:
            return False

    def vahingoita(self, määrä):
        try:
            if float(määrä) >= 0:
                if määrä >= 0:
                    printti = self.__laji+" lost "
                    self.__määrä = int(määrä)
                    if self.__hp <= self.__määrä:
                        printti += str(self.__hp)+" hp."
                        print(printti)
                        self.__hp = int(0)
                        print(self.__laji, "fainted!")
                        self.__fainted = True
                        return True

                    elif self.__hp > self.__määrä:
                        self.__hp -= self.__määrä
                        printti += str(self.__määrä)+" hp."
                        print(printti)
                        return True
                else:
                    return False
        except ValueError:
            return False
        else:
            return False

