"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**,
**prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului
şi adăugaţi aceste valori în lista creată.
"""


nume,prenume,inaltime,ocupatie = input("Introdu numele tau , prenumele , inaltimea , ocupatia ").split()
date_personale = [nume,prenume,inaltime,ocupatie]
print(date_personale)

