import random

#GLOBAL: Bedeutet, dass diese Werte immer gelten, sind Grundlagedaten
score = 0
background_color = color(173, 216, 230)  # Hellblauer Hintergrund

# Positive Areas = Liste aller Begriffe, welche einen Pluspunkt geben und sich grün einfärben werden
areas = [
    ["Fahrrad fahren", 1],
    ["Zug fahren", 2],
    ["Bus fahren", 1],
    ["Bei RICARDO bestellen", 1],
    ["Bei EBAY bestellen", 1],
    ["Ins Brocki gehen", 1],
    ["Regional einkaufen", 1],
    ["Gemüse kaufen", 1],
    ["Unverpackt", 1],
    ["Abfall trennen", 1],
    ["Glas anstatt Plastik", 1],
    ["Karton anstatt Plastik", 1],
    ["Heizung auf tiefer Stufe", 1],
    ["Alu anstatt Plastik", 2],
    ["Auto fahren", -2],
    ["Fliegen", -10],
    ["Bei SHEIN bestellen", -2],
    ["Bei H&M einkaufen", -1],
    ["Fleisch kaufen", -1],
    ["Plastikverpackung", -1],
    ["Motor laufen lassen", -3],
    ["Avocado kaufen", -5],
    ["Toilettenspühlung", -1],
    ["Kuehlschrank offen lassen", -1],
    ["Alu anstatt Glas", -1]
]

# Kombiniert beide Listen zu einer übergeordneten Liste, um die Funktionsanwendung zu vereinfachen
all_areas = []


# Generelle Grösse jedes Feldes
field_width = 150
field_height = 70

# Abstand zwischen den Feldern
horizontal_spacing = 180
vertical_spacing = 100

def setup():
    global all_areas  # es sollen immer "all_areas" verwendet werden
    
    size(1200, 700)  # SCanva Grösse
    textAlign(CENTER, CENTER) #Text soll immer zentriert sein in den Textfeldern
    textSize(12)  # Schriftgröße
    
    textFont(createFont("DejaVuSans", 12))
    
    # Befehl, dass beide Listen von oben kombiniert werden sollten
    all_areas = []
    random.shuffle(areas)
    i = 0
    
    # Felder einfügen: Zuerst die positiven Felder
    for element in areas:
        title = element[0].encode('utf-8').decode('utf-8') #FÜR UMLAUTE ABER FUNKTIONIEEEEERT NICHT
        x = 100 + (i % 5) * horizontal_spacing  # Berechne den x-Wert für bis zu 5 Felder pro Zeile
        y = 100 + (i // 5) * vertical_spacing  # Berechne den y-Wert, um in mehreren Zeilen zu platzieren
        all_areas.append([x, y, field_width, field_height, title, False, element[1]])  # Füge das positive Feld zu all_areas hinzu
        i += 1
    
    # Dann die negativen Felder
    # for i, title in enumerate(negative_areas):
    #     title[0] = title[0].encode('utf-8').decode('utf-8')
    #     x = 100 + (i % 5) * horizontal_spacing  # Berechne den x-Wert
    #     y = 100 + ((i + len(positive_areas)) // 5) * vertical_spacing  # Berechne den y-Wert für negative Felder
    #     all_areas.append([x, y, field_width, field_height, title[0], False, -1])  # Füge das negative Feld zu all_areas hinzu

    print(all_areas)

def draw():
    background(background_color)  # Hintergrundfarbe zeichnen
    
    # Zeichne alle Felder
    for i, area in enumerate(all_areas):
        x = area[0]
        y = area[1]
        
        # Setze die Farben je nach Status
        if area[5]:  # Wenn das Feld angeklickt wurde
            if area[6] > 0:  # Positives Feld
                fill(0, 255, 0)  # Grün für positive Felder
            else:  # Negatives Feld
                fill(255, 0, 0)  # Rot für negative Felder
        else:  # Wenn das Feld noch nicht angeklickt wurde
            fill(255)  # Weiß für Felder, die nicht angeklickt wurden
        
        rect(x, y, area[2], area[3])  # Rechteck für das Feld zeichnen
        fill(0)
        textSize(12)  # Schriftgröße für die Felder bleibt 12
        text(area[4], x + area[2] / 2, y + area[3] / 2)  # Text auf dem Feld
        
    # Zeige die Punktzahl oben in der Mitte an
    fill(0)
    textSize(30)  # Schriftgröße für die Punktzahl bleibt 12
    text("Punkte: " + str(score), width / 2, 40)
    
    # Wenn die Punktzahl über 10 steigt, zeige den Text an
    if score > 10:
        textSize(30)  # Schriftgröße für den Text ist 30
        fill(0)  # Schwarzer Text
        text("Super! Unsere Erde sagt danke für deinen Einsatz! :)", width / 2, height - 40)  # Text unten zentriert

def mousePressed():
    global score, background_color
    
    for i, area in enumerate(all_areas):
        x = area[0]
        y = area[1]

        if mouseX > x and mouseX < x + area[2] and mouseY > y and mouseY < y + area[3]:
            if not area[5]:  # Nur wenn das Feld noch nicht angeklickt wurde
                score += area[6]  # Punkte entsprechend der Felder (positiv oder negativ)
                area[5] = True  # Markiere das Feld als angeklickt
                
                # Setze Hintergrundfarbe basierend auf der Art des Feldes
                if area[6] > 0:  # Positives Feld
                    background_color = color(144, 238, 144)  # Hellgrün für positive Auswahl
                else:  # Negatives Feld
                    background_color = color(255, 165, 0)  # Hellorange für negative Auswahl
            break
