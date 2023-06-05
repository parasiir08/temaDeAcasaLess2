"""Scrieţi un program care citeşte de la tastatură
de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

x,y,z = map(int, input("Introdu prin spatiu de 3 ori timpul de secunde pe care-l alearga sportivul la proba de 100 metri ").split())
media= (x+y+z)/3
print(f"Media aritmetica este {media}")
