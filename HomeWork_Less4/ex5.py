"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""

punctaj = int(input("Introdu numarul de puncte acumulate "))
if punctaj>15:
    print("Nota este trecatoare")
elif punctaj==15:
    print("Ai trecut testul")
else:
    print("Va mai trebuie sa resustii testul")
