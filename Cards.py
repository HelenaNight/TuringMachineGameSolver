def karte_1(code):
    return f"d {'> 1' if int(code[0]) > 1 else '= 1'}"

def karte_2(code):
    zahl = int(code[0])
    if zahl < 3:
        return "d < 3"
    elif zahl > 3:
        return "d > 3"
    else:
        return "d = 3"

def karte_3(code):
    zahl = int(code[1])
    if zahl < 3:
        return "q < 3"
    elif zahl > 3:
        return "q > 3"
    else:
        return "q = 3"

def karte_4(code):
    zahl = int(code[1])
    if zahl < 4:
        return "q < 4"
    elif zahl > 4:
        return "q > 4"
    else:
        return "q = 4"

def karte_5(code):
    return f"Dreieck ist {'gerade' if int(code[0]) % 2 == 0 else 'ungerade'}"

def karte_6(code):
    return f"Quadrat ist {'gerade' if int(code[1]) % 2 == 0 else 'ungerade'}"

def karte_7(code):
    return f"Kreis ist {'gerade' if int(code[2]) % 2 == 0 else 'ungerade'}"

def karte_8(code):
    return f"{code.count('1')} x1en"

def karte_9(code):
    return f"{code.count('3')} x3en"

def karte_10(code):
    return f"{code.count('4')} x4en"

def karte_11(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    if dreieck < quadrat:
        return "d < q"
    elif dreieck > quadrat:
        return "d > q"
    else:
        return "d = q"

def karte_12(code):
    dreieck = int(code[0])
    kreis = int(code[2])
    if dreieck < kreis:
        return "d < k"
    elif dreieck > kreis:
        return "d > k"
    else:
        return "d = k"

def karte_13(code):
    quadrat = int(code[1])
    kreis = int(code[2])
    if quadrat < kreis:
        return "q < k"
    elif quadrat > kreis:
        return "q > k"
    else:
        return "q = k"

def karte_14(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    kreis = int(code[2])
    werte = [dreieck, quadrat, kreis]
    if werte.count(min(werte)) == 1:
        if min(werte) == dreieck:
            return "min: d"
        elif min(werte) == quadrat:
            return "min: q"
        else:
            return "min: k"
    else:
        return "Fehler"

def karte_15(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    kreis = int(code[2])
    werte = [dreieck, quadrat, kreis]
    if werte.count(max(werte)) == 1:
        if max(werte) == dreieck:
            return "Max: d"
        elif max(werte) == quadrat:
            return "Max: q"
        else:
            return "Max: k"
    else:
        return "Fehler"

def karte_16(code):
    zahlen = [int(code[0]), int(code[1]), int(code[2])]
    gerade = sum(1 for z in zahlen if z % 2 == 0)
    ungerade = 3 - gerade
    if gerade > ungerade:
        return "Mehr gerade"
    elif gerade < ungerade:
        return "Mehr ungerade"
    else:
        return "Gleich viele gerade wie ungerade Zahlen"

def karte_17(code):
    zahlen = [int(code[0]), int(code[1]), int(code[2])]
    gerade = sum(1 for z in zahlen if z % 2 == 0)
    return f"{gerade} gerade"

def karte_18(code):
    zahlen = [int(code[0]), int(code[1]), int(code[2])]
    gesamt = sum(zahlen)
    return f"d+q+k ist {'gerade' if gesamt % 2 == 0 else 'ungerade'}"

def karte_19(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    summe = dreieck + quadrat
    if summe < 6:
        return "d + q < 6"
    elif summe > 6:
        return "d + q > 6"
    else:
        return "d + q = 6"

def karte_20(code):
    zahlen = [code[0], code[1], code[2]]
    einzigartig = len(set(zahlen))
    if einzigartig == 3:
        return "0 gleiche Zahlen"
    elif einzigartig == 2:
        return "2 gleiche Zahlen"
    else:
        return "3 gleiche Zahlen"
    
def karte_21(code):
    zahlen = [code[0], code[1], code[2]]
    einzigartig = len(set(zahlen))
    if einzigartig == 2:
        return "Paar"
    else:
        return "kein Paar"

def karte_22(code):
    d, q, k = int(code[0]), int(code[1]), int(code[2])
    if d < q < k:
        return "aufsteigend"
    elif d > q > k:
        return "absteigend"
    else:
        return "unsortiert"


def karte_23(code):
    gesamt = sum(int(z) for z in code)
    if gesamt < 6:
        return "d+q+k < 6"
    elif gesamt > 6:
        return "d+q+k > 6"
    else:
        return "d+q+k = 6"

def karte_24(code):
    z = [int(code[0]), int(code[1]), int(code[2])]
    count = 0
    if z[1] == z[0] + 1:
        count += 1
    if z[2] == z[1] + 1:
        count += 1
    return f"{count + 1 if count > 0 else 0} aufsteigend"

def karte_25(code):
    z = [int(code[0]), int(code[1]), int(code[2])]

    # Prüfe erste und zweite Zahl
    erste_folge = abs(z[1] - z[0]) == 1
    zweite_folge = abs(z[2] - z[1]) == 1

    if erste_folge and zweite_folge:
        return "3 auf/ab"
    elif erste_folge or zweite_folge:
        return "2 auf/ab"
    else:
        return "0 auf/ab"
    
def karte_26(code):
    result = []
    if int(code[0]) < 3:
        result.append("Dreieck")
    if int(code[1]) < 3:
        result.append("Quadrat")
    if int(code[2]) < 3:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_27(code):
    result = []
    if int(code[0]) < 4:
        result.append("Dreieck")
    if int(code[1]) < 4:
        result.append("Quadrat")
    if int(code[2]) < 4:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_28(code):
    result = []
    if int(code[0]) == 1:
        result.append("Dreieck")
    if int(code[1]) == 1:
        result.append("Quadrat")
    if int(code[2]) == 1:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_29(code):
    result = []
    if int(code[0]) == 3:
        result.append("Dreieck")
    if int(code[1]) == 3:
        result.append("Quadrat")
    if int(code[2]) == 3:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_30(code):
    result = []
    if int(code[0]) == 4:
        result.append("Dreieck")
    if int(code[1]) == 4:
        result.append("Quadrat")
    if int(code[2]) == 4:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_31(code):
    result = []
    if int(code[0]) > 1:
        result.append("Dreieck")
    if int(code[1]) > 1:
        result.append("Quadrat")
    if int(code[2]) > 1:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_32(code):
    result = []
    if int(code[0]) > 3:
        result.append("Dreieck")
    if int(code[1]) > 3:
        result.append("Quadrat")
    if int(code[2]) > 3:
        result.append("Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_33(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    kreis = int(code[2])
    return (
        f"Dreieck {'gerade' if dreieck % 2 == 0 else 'ungerade'}, "
        f"Quadrat {'gerade' if quadrat % 2 == 0 else 'ungerade'}, "
        f"Kreis {'gerade' if kreis % 2 == 0 else 'ungerade'}"
    )

def karte_34(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    kreis = int(code[2])
    min_wert = min(dreieck, quadrat, kreis)
    result = []
    if dreieck == min_wert:
        result.append("Dreieck")
    if quadrat == min_wert:
        result.append("Quadrat")
    if kreis == min_wert:
        result.append("Kreis")
    return " , ".join(result)

def karte_35(code):
    dreieck = int(code[0])
    quadrat = int(code[1])
    kreis = int(code[2])
    max_wert = max(dreieck, quadrat, kreis)
    result = []
    if dreieck == max_wert:
        result.append("Dreieck")
    if quadrat == max_wert:
        result.append("Quadrat")
    if kreis == max_wert:
        result.append("Kreis")
    return  " , ".join(result)

def karte_36(code):
    gesamt = sum(int(z) for z in code)
    teilbar = []
    for n in [3, 4, 5]:
        if gesamt % n == 0:
            teilbar.append(str(n))
    return  ", ".join(teilbar) if teilbar else "Fehler"

def karte_37(code):
    d, q, k = int(code[0]), int(code[1]), int(code[2])
    result = []
    if d + q == 4:
        result.append("Dreieck + Quadrat")
    if d + k == 4:
        result.append("Dreieck + Kreis")
    if q + k == 4:
        result.append("Quadrat + Kreis")
    return ", ".join(result)  if result else "Fehler"

def karte_38(code):
    d, q, k = int(code[0]), int(code[1]), int(code[2])
    result = []
    if d + q == 6:
        result.append("Dreieck + Quadrat")
    if d + k == 6:
        result.append("Dreieck + Kreis")
    if q + k == 6:
        result.append("Quadrat + Kreis")
    return ", ".join(result) if result else "Fehler"

def karte_39(code):
    result = []
    for name, zahl in zip(["Dreieck", "Quadrat", "Kreis"], map(int, code)):
        if zahl == 1:
            result.append(f"{name} = 1")
        else:
            result.append(f"{name} > 1")
    return ", ".join(result)

def karte_40(code):
    result = []
    for name, zahl in zip(["Dreieck", "Quadrat", "Kreis"], map(int, code)):
        if zahl == 3:
            result.append(f"{name} = 3")
        elif zahl > 3:
            result.append(f"{name} > 3")
        else:
            result.append(f"{name} < 3")
    return ", ".join(result)

def karte_41(code):
    result = []
    for name, zahl in zip(["Dreieck", "Quadrat", "Kreis"], map(int, code)):
        if zahl == 4:
            result.append(f"{name} = 4")
        elif zahl > 4:
            result.append(f"{name} > 4")
        else:
            result.append(f"{name} < 4")
    return ", ".join(result)

def karte_42(code):
    dreieck, quadrat, kreis = map(int, code)
    werte = [dreieck, quadrat, kreis]

    result = []

    min_wert = min(werte)
    max_wert = max(werte)
    
    min_zähler = werte.count(min_wert)
    if min_zähler == 1:
        if dreieck == min_wert:
            result.append("Min: Dreieck")
        elif quadrat == min_wert:
            result.append("Min: Quadrat")
        elif kreis == min_wert:
            result.append("Min: Kreis")

    max_zähler = werte.count(max_wert)
    if max_zähler == 1:
        if dreieck == max_wert:
            result.append("Max: Dreieck")
        elif quadrat == max_wert:
            result.append("Max: Quadrat")
        elif kreis == max_wert:
            result.append("Max: Kreis")

    return ", ".join(result) if result else "Fehler"

def karte_43(code):
    dreieck, quadrat, kreis = map(int, code)
    vergleiche = []
    if dreieck < quadrat:
        vergleiche.append("Dreieck < Quadrat")
    elif dreieck > quadrat:
        vergleiche.append("Dreieck > Quadrat")
    else:
        vergleiche.append("Dreieck = Quadrat")

    if dreieck < kreis:
        vergleiche.append("Dreieck < Kreis")
    elif dreieck > kreis:
        vergleiche.append("Dreieck > Kreis")
    else:
        vergleiche.append("Dreieck = Kreis")

    return ", ".join(vergleiche)

def karte_44(code):
    dreieck, quadrat, kreis = map(int, code)
    vergleiche = []
    if quadrat < dreieck:
        vergleiche.append("Quadrat < Dreieck")
    elif quadrat > dreieck:
        vergleiche.append("Quadrat > Dreieck")
    else:
        vergleiche.append("Quadrat = Dreieck")

    if quadrat < kreis:
        vergleiche.append("Quadrat < Kreis")
    elif quadrat > kreis:
        vergleiche.append("Quadrat > Kreis")
    else:
        vergleiche.append("Quadrat = Kreis")

    return ", ".join(vergleiche)

def karte_45(code):
    einsen = code.count('1')
    dreien = code.count('3')
    return f"{einsen}x1en, {dreien}x3en"

def karte_46(code):
    dreien = code.count('3')
    vieren = code.count('4')
    return f"{dreien}x3en, {vieren}x4en"

def karte_47(code):
    einsen = code.count('1')
    vieren = code.count('4')
    return f"{einsen}x1en, {vieren}x4en"

def karte_48(code):
    dreieck, quadrat, kreis = map(int, code)
    vergleiche = []

    # Dreieck vs Quadrat
    if dreieck < quadrat:
        vergleiche.append("Dreieck < Quadrat")
    elif dreieck > quadrat:
        vergleiche.append("Dreieck > Quadrat")
    else:
        vergleiche.append("Dreieck = Quadrat")

    # Dreieck vs Kreis
    if dreieck < kreis:
        vergleiche.append("Dreieck < Kreis")
    elif dreieck > kreis:
        vergleiche.append("Dreieck > Kreis")
    else:
        vergleiche.append("Dreieck = Kreis")

    # Quadrat vs Kreis
    if quadrat < kreis:
        vergleiche.append("Quadrat < Kreis")
    elif quadrat > kreis:
        vergleiche.append("Quadrat > Kreis")
    else:
        vergleiche.append("Quadrat = Kreis")

    return ", ".join(vergleiche)

