def ahaa(toisto):
    i = 0
    for i in range(0,toisto):
        print("ahaa")

def säkeistö(line1,line2):
    for i in range(0, 2):
        print(line1)
        ahaa(2)
    print(line1)
    print(line2)
    ahaa(3)
    print()

def main():
    line1 = "saku sammakko kosiomatkallaan"
    line2 = "hän lauleli kauniita laulujaan"
    säkeistö(line1, line2)
    line1 = "hän hillevi hiiren tavatessaan"
    line2 = "pyysi mukanaan tulemaan pappilaan"
    säkeistö(line1,line2)
    line1 = "mikset kultasein kosinut aikanaan"
    line2 = "minut matias myyrälle naitetaan"
    säkeistö(line1,line2)
    line1 = "sulle matias sovi ei laisinkaan"
    line2 = "sillä multaa on myyrällä varpaissaan"
    säkeistö(line1,line2)


main()
