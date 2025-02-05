
def berechne_sternzeichen(tag, monat):
    # Sternzeichen-Daten
    sternzeichen = {
        "Widder": [(3, 21), (4, 19)],
        "Stier": [(4, 20), (5, 20)],
        "Zwillinge": [(5, 21), (6, 20)],
        "Krebs": [(6, 21), (7, 22)],
        "Löwe": [(7, 23), (8, 22)],
        "Jungfrau": [(8, 23), (9, 22)],
        "Waage": [(9, 23), (10, 22)],
        "Skorpion": [(10, 23), (11, 21)],
        "Schütze": [(11, 22), (12, 21)],
        "Steinbock": [(12, 22), (1, 19)],
        "Wassermann": [(1, 20), (2, 18)],
        "Fische": [(2, 19), (3, 20)]
    }

    for stern, (anfang, ende) in sternzeichen.items():
        # Überprüfen, ob das Datum im Bereich des Sternzeichens liegt
        if (monat == anfang[0] and tag >= anfang[1]) or (monat == ende[0] and tag <= ende[1]) or (monat > anfang[0] and monat < ende[0]):
            return stern
    return None

while True:
    print("Sternzeichen Berechnungsprogramm")
    print("Drücke 0, um das Programm zu beenden.")

    try:
        tag = int(input("Gib deinen Geburtstag (Tag) ein: "))
        if tag == 0:
            break
        monat = int(input("Gib deinen Geburtsmonat (1-12) ein: "))
        if monat == 0:
            break

        sternzeichen = berechne_sternzeichen(tag, monat)
        if sternzeichen:
            print(f"Dein Sternzeichen ist: {sternzeichen}")
        else:
            print("Ungültiges Datum! Bitte gib ein korrektes Datum ein.")
    except ValueError:
        print("Ungültige Eingabe! Bitte gib eine gültige Zahl ein.")
