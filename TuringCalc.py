
import copy
from collections import Counter, defaultdict
from itertools import product

import Cards


def parse_karten_input(eingabe):
    try:
        zahlen = list(map(int, eingabe.strip().split()))
        if all(1 <= z <= 48 for z in zahlen) and 4 <= len(zahlen) <= 6:
            return zahlen
        else:
            print("Bitte gib 4 bis 6 Zahlen zwischen 1 und 48 ein.")
            return None
    except ValueError:
        print("Ungültige Eingabe. Bitte gib Zahlen ein.")
        return None


def berechnung_fuer_karte(karte, code):
    func = getattr(Cards, f"karte_{karte}", None)
    return func(code) if func else f"Karte {karte}: Ungültige Karte"


def kombis_berechnen(karten):
    kombis = []
    ergebnis_counter = Counter()

    for d, q, k in product(range(1, 6), repeat=3):
        code = f"{d}{q}{k}"
        antworten = {}
        fehler = False

        for karte in karten:
            result = berechnung_fuer_karte(karte, code)
            if "Fehler" in result:
                fehler = True
                break
            antworten[karte] = result.replace(f"Karte {karte}: ", "")

        if fehler:
            continue

        identifikation = " | ".join([antworten[k] for k in karten])
        ergebnis_counter[identifikation] += 1

        kombis.append({
            "code": code,
            "antworten": antworten,
            "identifikation": identifikation
        })

    eindeutige_kombis = [
        eintrag for eintrag in kombis if ergebnis_counter[eintrag["identifikation"]] == 1
    ]

    return eindeutige_kombis


def statistik_berechnen(karten, kombis):
    statistik = {karte: defaultdict(int) for karte in karten}
    for eintrag in kombis:
        for karte in karten:
            aussage = eintrag["antworten"][karte]
            statistik[karte][aussage] += 1
    return statistik


def zeige_kombis(kombis):
    print("\nFolgende Zahlenkombinationen sind noch möglich:\n")
    for eintrag in kombis:
        code = eintrag["code"]
        print(f"{code[0]}-{code[1]}-{code[2]} → {eintrag['identifikation']}")


def zeige_statistik(karten, statistik):
    print("\nAuswertung der Ergebnisse je Karte:")
    for karte in karten:
        werte = statistik[karte]
        if len(werte) <= 1:
            print(f"Für Karte {karte} gibt nur noch eine Kombi also irrelevant")
        else:
            print(f"Für Karte {karte} gibt es:")
            for aussage, anzahl in werte.items():
                print(f"{anzahl}x \"{aussage}\"")


def spiel_starten():
    default_karten = [1, 4, 12, 22]
    print("Hallo mit welchen Karten spielen wir?")
    eingabe = input("(Gib 'd' für Default-Karten ein): ").strip().lower()
    if eingabe == 'd':
        print(f"Okay, wir spielen mit den Default-Karten {default_karten}")
        return default_karten

    karten = parse_karten_input(eingabe)
    while karten is None:
        eingabe = input("Versuche es nochmal: ")
        karten = parse_karten_input(eingabe)
    print("Danke, die Karten wurden gespeichert")
    return karten


def code_wählen(kombis):
    gültige_codes = {eintrag["code"] for eintrag in kombis}
    while True:
        eingabe = input("\nGib einen Code ein (z. B. 1-1-4): ").strip().lower()
        if len(eingabe) == 5 and eingabe[1] == '-' and eingabe[3] == '-':
            teile = eingabe.split('-')
            if all(t.isdigit() and 1 <= int(t) <= 5 for t in teile):
                code_str = "".join(teile)
                if code_str in gültige_codes:
                    return code_str
                else:
                    print("Dieser Code ist nicht in der Liste gültiger Kombinationen.")
        print("Ungültiger Code. Format: z. B. 1-3-4")


def bereinige_aussagen(kombis, antwort_speicher):
    bereinigte = []

    for eintrag in kombis:
        gültig = True
        for karte, aussage in list(eintrag["antworten"].items()):
            teile = [t.strip() for t in aussage.split(",")]
            gültige_teile = [
                teil for teil in teile
                if not any(teil == nein_teil.strip()
                           for n in antwort_speicher[karte]["nein"]
                           for nein_teil in n.split(","))
            ]
            if not gültige_teile:
                gültig = False
                break
            eintrag["antworten"][karte] = ", ".join(gültige_teile)

        if gültig:
            eintrag["identifikation"] = " | ".join(
                eintrag["antworten"][k] for k in sorted(eintrag["antworten"].keys())
            )
            bereinigte.append(eintrag)

    kombis.clear()
    kombis.extend(bereinigte)


def finde_relevante_teilaussagen(antwort_speicher, karte):
    ja_aussagen = [s.split(",") for s in antwort_speicher[karte]["ja"]]
    ja_sets = [set(teil.strip() for teil in gruppe) for gruppe in ja_aussagen]

    if len(ja_sets) < 2:
        return

    schnittmenge = set.intersection(*ja_sets)

    if schnittmenge:
        antwort_speicher[karte]["ja"] = {
            ", ".join(sorted(schnittmenge))
        }


def reduziere_jas_durch_neins(antwort_speicher, karte):
    neue_jas = set()

    ja_liste = list(antwort_speicher[karte]["ja"])
    nein_liste = list(antwort_speicher[karte]["nein"])

    for ja in ja_liste:
        ja_set = set(t.strip() for t in ja.split(","))
        for nein in nein_liste:
            nein_set = set(t.strip() for t in nein.split(","))
            schnitt = ja_set & nein_set
            unterschied_ja = ja_set - nein_set
            unterschied_nein = nein_set - ja_set

            if len(unterschied_ja) == 1 and len(unterschied_nein) == 1 and schnitt:
                neue_jas.add(list(unterschied_ja)[0])

    if neue_jas:
        antwort_speicher[karte]["ja"] = neue_jas


def antwort_verarbeiten(code, karten, kombis, karte_map, antwort_speicher):
    eintrag = next((e for e in kombis if e["code"] == code), None)
    if not eintrag:
        print("Code nicht gefunden.")
        return kombis

    print(f"Okay, du hast Code {code[0]}-{code[1]}-{code[2]} gewählt.")
    interaktionen = 0

    while interaktionen < 3:
        aktion = input("Gib eine Karte (A, B, C...) mit der Antwort (ja/nein), 'c' für neuen Code oder 'x': ").strip().lower()
        if aktion == 'x':
            exit()
        elif aktion == 'c':
            return kombis
        elif len(aktion) >= 3 and aktion[0].upper() in karte_map and aktion[2:] in ["ja", "nein"]:
            buchstabe = aktion[0].upper()
            antwort = aktion[2:]
            karte_nr = karte_map[buchstabe]
            aussage = eintrag["antworten"][karte_nr]
            print(f"Okay, {buchstabe} ist Karte {karte_nr}, das bedeutet, dass \"{aussage}\" {'richtig' if antwort == 'ja' else 'falsch'} ist.")

            relevante_teile = set(t.strip() for t in aussage.split(","))
            neue_kombis = []

            if antwort == "ja":
                for e in kombis:
                    teile = [t.strip() for t in e["antworten"][karte_nr].split(",")]
                    reduzierte = [t for t in teile if t in relevante_teile]
                    if reduzierte:
                        e["antworten"][karte_nr] = ", ".join(reduzierte)
                        neue_kombis.append(e)
            else:
                for e in kombis:
                    teile = [t.strip() for t in e["antworten"][karte_nr].split(",")]
                    reduzierte = [t for t in teile if t not in relevante_teile]
                    if reduzierte:
                        e["antworten"][karte_nr] = ", ".join(reduzierte)
                        neue_kombis.append(e)

            kombis = [e for e in neue_kombis if all(e["antworten"][k].strip() != "" for k in karten)]

            kombis = check_for_unidentifiable(kombis)

            zeige_kombis(kombis)
            statistik = statistik_berechnen(karten, kombis)
            zeige_statistik(karten, statistik)
            if len(kombis) == 1:
                code = kombis[0]["code"]
                print(f"\nHerzlichen Glückwunsch dein Code ist: {code[0]}-{code[1]}-{code[2]}")
                exit()

            interaktionen += 1
        else:
            print("Ungültige Eingabe. Beispiel: A ja oder B nein oder 'c' oder 'x'")
    return kombis

def check_for_unidentifiable(kombis):
    for e in kombis:
        e["identifikation"] = " | ".join(e["antworten"][k] for k in sorted(e["antworten"].keys()))
    ident_counter = Counter([k["identifikation"] for k in kombis])
    doppelte_identifikationen = {ident for ident, count in ident_counter.items() if count > 1}
    gefiltert = [k for k in kombis if k["identifikation"] not in doppelte_identifikationen]
    kombis_gefiltert = check_for_possible_unidentifiable(gefiltert)
    return kombis_gefiltert

def check_for_possible_unidentifiable(kombis):
    if not kombis:
        return kombis

    karten_keys = list(kombis[0]["antworten"].keys())
    kombis_überarbeitet = copy.deepcopy(kombis)

    for karte in karten_keys:
        antworten_k = [k["antworten"][karte] for k in kombis]
        unique_antworten = set(antworten_k)

        if len(unique_antworten) == 1 and "," not in next(iter(unique_antworten)):
            continue

        try:
            sets_pro_kombi = [set(t.strip() for t in ans.split(",")) for ans in antworten_k]
        except Exception:
            continue

        gemeinsame_elemente = set.intersection(*sets_pro_kombi)

        if gemeinsame_elemente:
            for element in gemeinsame_elemente:
                kombis_temp = copy.deepcopy(kombis)
                for k in kombis_temp:
                    k["antworten"][karte] = element

                result = check_for_unidentifiable(kombis_temp)

                if not result:
                    print(f"❌ Element '{element}' macht Kombis unidentifizierbar → wird entfernt.")
                    for k in kombis_überarbeitet:
                        aktuelle_set = set(k["antworten"][karte].split(","))
                        bereinigt = aktuelle_set - {element}
                        k["antworten"][karte] = ",".join(bereinigt) if bereinigt else ""

                    kombis_überarbeitet = [
                        k for k in kombis_überarbeitet if all(a.strip() != "" for a in k["antworten"].values())
                    ]

                    kombis_überarbeitet = check_for_unidentifiable(kombis_überarbeitet)

    return kombis_überarbeitet



def main():
    karten = spiel_starten()
    kombis = kombis_berechnen(karten)
    antwort_speicher = {karte: {"ja": set(), "nein": set()} for karte in karten}

    zeige_kombis(kombis)
    statistik = statistik_berechnen(karten, kombis)
    zeige_statistik(karten, statistik)

    buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    karte_map = {buchstaben[i]: karten[i] for i in range(len(karten))}
    print("\nKartenzuordnung:")
    for b, k in karte_map.items():
        print(f"{b} = Karte {k}")

    while True:
        code = code_wählen(kombis)
        if code is None:
            break
        elif code == "wechseln":
            continue
        kombis = antwort_verarbeiten(code, karten, kombis, karte_map, antwort_speicher)
        if not kombis:
            print("Keine gültigen Kombinationen mehr vorhanden.")
            break


if __name__ == "__main__":
    main()
