def main():
    for i in range(1, 11):
        for j in range(1, 11):
            tulo = i * j
            print("{:4d}".format(tulo), end="")
        print()

main()