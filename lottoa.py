from math import factorial
def tarkista(n,p):
    if p < 0 or n < 0:
        print("Pallojen määrän oltava positiivinen luku.")
    elif p > n:
        print("Arvottavia palloja saa olla enintään pallojen kokonaismäärän verran.")

    else:
        a = True
        return a

def laske(n,p):
    t = int(n-p)
    nimittäjä = int((factorial(n))/ (factorial(t) * factorial(p)))
    return nimittäjä



def main():
    a = 0
    n = int(input("Syötä lottopallojen kokonaismäärä: "))
    p = int(input("Syötä arvottavien pallojen määrä: "))
    a = tarkista(n,p)
    if a == True:
        nimittäjä = str(laske(n,p))
        p = str(p)
        print("Kun pelataan yksi rivi, todennäköisyys saada "+p+" oikein on 1/"+nimittäjä)

main()