
EPSILON = 0.000000001
def vertaile(a,b):
    c = a - b
    c = abs(c)
    if c < EPSILON:
        tulos = 1
    elif c > EPSILON:
        tulos = 0
    return tulos


# määrittele tänne funktio vertailu tehtävänannon mukaisesti

def main():
    a = float(input("Anna liukuluku A: "))
    b = float(input("Anna liukuluku B: "))
    tulos = vertaile(a,b)
    if tulos == 0:
        print("Luvut eivät ole samat!")
    if tulos == 1:
        print("Luvut ovat samat!")
main()