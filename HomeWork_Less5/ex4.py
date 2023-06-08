"""
Creaţi 2 liste: `elev1` şi `elev2`.
Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele
în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule,
iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""
elev1 = []
elev2 = []
# Citirea datelor pentru primul elev
nume, prenume, nota = input("Introduceti numele, prenumele si nota pentru primul elev: ").split()
elev1.extend([nume.upper(), prenume.capitalize(), float(nota)])
# Citirea datelor pentru al doilea elev
nume, prenume, nota = input("Introduceti numele, prenumele si nota pentru al doilea elev: ").split()
elev2.extend([nume.upper(), prenume.capitalize(), float(nota)])

# Afișarea elevului cu nota mai mare
if elev1[2] > elev2[2]:
    print(f"Elevul {elev1[0]} {elev1[1]} are o nota mai mare la examen")
elif elev1[2] < elev2[2]:
    print(f"Elevul {elev2[0]} {elev2[1]} are o nota mai mare la examen")

# Afișarea elevului cu nota mai mică
if elev1[2] < elev2[2]:
    print(f"Elevul {elev1[0]} {elev1[1]} are o nota mai mica la examen")
elif elev1[2] > elev2[2]:
    print(f"Elevul {elev2[0]} {elev2[1]} are o nota mai mica la examen")

# Transformarea numelui și prenumelui
elev1[0] = elev1[0].title()
elev2[0] = elev2[0].title()
elev1[1] = elev1[1].upper()
elev2[1] = elev2[1].upper()

# Afișarea datelor sub formă de tabel
print("| {:<10} | {:<10} | {:<10.1f} |".format(elev1[0], elev1[1], elev1[2]))
print("|------------|------------|------------|")
print("| {:<10} | {:<10} | {:<10.1f} |".format(elev2[0], elev2[1], elev2[2]))
