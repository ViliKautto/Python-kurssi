def pisin_jarjestetty_alimerkkijono(syöte):
    aakkoset = "abcdefghijklmnopqrstuvwxyzåäö"
    syöte = syöte.strip(",")
    ainoa_merkki=[]
    i = 1
    p = len(syöte)
    if len(syöte) == 1:
        return syöte
    if len(syöte) == 0:
        return syöte
    else:
        mjono = syöte[0]
        jono = ""
        while i < p:
            k1 = syöte[i]
            k2 = syöte[i-1]
            if aakkoset.index(k2) < aakkoset.index(k1):
                mjono = mjono + k1
                if len(mjono) > len(jono):
                    jono = mjono
            else:
                ainoa_merkki.append(k2)
                mjono = k1
            i += 1
        if len(jono) == 0:
            jono = (ainoa_merkki[0])
        return jono