def laske_abbat(sana):
    i = 0
    lkm = 0
    p = len(sana)
    while i < p-3:
        if sana[i] == "a" and sana[i+1] == "b" and sana[i+2] == "b" and sana[i+3] == "a":
            lkm += 1
        i += 1
    return lkm
