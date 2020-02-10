class Murtoluku:

    def __init__(self, osoittaja, nimittäjä):

        if not isinstance(osoittaja, int) or not isinstance(nimittäjä, int):
            raise TypeError
        elif nimittäjä == 0:
            raise ValueError

        nimittäjä = nimittäjä
        osoittaja = osoittaja
        self.__osoittaja = osoittaja
        self.__nimittäjä = nimittäjä

    def __lt__(self, mluku2):
            return self.erota(mluku2) < 0

    def tulosta(self):

        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = "-"
        else:
            etumerkki = ""
        return("{:s}{:d}/{:d}".format(etumerkki, abs(self.__osoittaja),
                                     abs(self.__nimittäjä)))

    def sievenna(self):
        self.__syt = suurin_yhteinen_tekijä(self.__osoittaja, self.__nimittäjä)
        self.__osoittaja = self.__osoittaja // self.__syt
        self.__nimittäjä = self.__nimittäjä // self.__syt

    def vastaluku(self):
        self.__osoittaja = int(-1*self.__osoittaja)
        return Murtoluku(self.__osoittaja, self.__nimittäjä)

    def kaanteisluku(self):
        self.__uusi_osoittaja = self.__nimittäjä
        self.__uusi_nimittäjä = self.__osoittaja
        self.__osoittaja = self.__uusi_osoittaja
        self.__nimittäjä = self.__uusi_nimittäjä
        return Murtoluku(self.__osoittaja, self.__nimittäjä)

    def kerro(self,mluku2):
        self.__osoittaja2 = mluku2._Murtoluku__osoittaja
        self.__nimittäjä2 = mluku2._Murtoluku__nimittäjä
        self.__osoittaja = self.__osoittaja*self.__osoittaja2
        self.__nimittäjä = self.__nimittäjä*self.__nimittäjä2
        return Murtoluku(self.__osoittaja,self.__nimittäjä)

    def jaa(self, mluku2):
        kertoja = mluku2.kaanteisluku()
        self.__osoittaja2 = kertoja._Murtoluku__osoittaja
        self.__nimittäjä2 = kertoja._Murtoluku__nimittäjä
        self.__osoittaja = self.__osoittaja * self.__osoittaja2
        self.__nimittäjä = self.__nimittäjä * self.__nimittäjä2
        return Murtoluku(self.__osoittaja, self.__nimittäjä)

    def summaa(self, mluku2):
        self.__osoittaja2 = mluku2._Murtoluku__osoittaja
        self.__nimittäjä2 = mluku2._Murtoluku__nimittäjä
        self.__uusi_osoittaja = self.__osoittaja * self.__nimittäjä2 + self.__osoittaja2 * self.__nimittäjä
        self.__uusi_nimittäjä = self.__nimittäjä * self.__nimittäjä2
        return Murtoluku(self.__uusi_osoittaja, self.__uusi_nimittäjä)


    def erota(self, mluku2):
        self.__osoittaja2 = mluku2._Murtoluku__osoittaja
        self.__nimittäjä2 = mluku2._Murtoluku__nimittäjä
        self.__uusi_osoittaja = self.__osoittaja * self.__nimittäjä2 - self.__osoittaja2 * self.__nimittäjä
        self.__uusi_nimittäjä = self.__nimittäjä * self.__nimittäjä2
        return Murtoluku(self.__uusi_osoittaja, self.__uusi_nimittäjä)


def suurin_yhteinen_tekijä(a, b):

    while b != 0:
        a, b = b, a % b
    return a
