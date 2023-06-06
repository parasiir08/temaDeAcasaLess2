"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat
în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temperatura= float(input("Introdu temperatura in *C "))
if temperatura >= -40 and temperatura <-10:
    print("Vremea este extrem de rece")
elif temperatura >=-10 and temperatura < 0:
    print("Vremea este foarte rece")
elif temperatura>=0 and temperatura<10:
    print("Vremea este normala")
elif temperatura>=20 and temperatura<30:
    print("Vremea este calda")
elif temperatura>=30 and temperatura<40:
    print("Este foarte cald")
elif temperatura>=40:
    print("Este extrem de cald")
