'''Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
'''
user_time_pref = int(input("In care format doresti sa fie afisat timpul: 12 sau in 24 ore ? "))

if user_time_pref == 12:
    timpul = input("Introdu timpul in formatul 12h: ")
    ore_minute = timpul.split(":")
    ore, minute = int(ore_minute[0]), int(ore_minute[1])
    if ore <= 11 and minute <= 59:
        print(f" Timpul este {ore}:{minute} AM")
    elif ore == 00 and minute <=59:
        print(f"Timpul este {ore}:{minute} AM")
    elif ore >= 12 and minute <= 59:
        print(f" Timpul este {ore}:{minute} PM")

if user_time_pref == 24:
    timpul = input("Introdu timpul in formatatul 24h: ")
    ore_minute = timpul.split(":")
    ore, minute = int(ore_minute[0]), int(ore_minute[1])
    if ore < 24 and minute <= 59:
        print(f" Timpul este {ore}:{minute}")



#print(f"Ai introdus acest timp {ore}:{minute}")
