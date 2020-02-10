def järjestä_luvut_aakkosjärjestykseen(lukuja):
    espanja_suomi = {}
    espanja_suomi = sorted(lukuja, key = lambda lukuja: str(lukuja))
    return espanja_suomi

def main():
    lukuja = [10, 1, 101, 2, 111, 212, 100000, 22, 222, 112, 10101, 1100, 11, 0]
    print(järjestä_luvut_aakkosjärjestykseen(lukuja))
main()