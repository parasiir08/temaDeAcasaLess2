'''Convertor de timp V2

Scrie un program care preia timpul introdus de utilizator în următorul format:
"11:20 PM" sau "02:00 AM".
Și îl convertește în formatul de 24 de ore.
"23:20" sau "02:00"

Combină soluția cu soluția din lecția live
și permite utilizatorului să decidă ce conversie să facă.
De la 24 de ore la 12 ore, sau invers.
'''
timp_input = input("Introduceți timpul în formatul HH:MM AM/PM: ")

if ":" not in timp_input or "AM" not in timp_input and "PM" not in timp_input:
    print("Formatul timpului introdus este invalid.")
else:
    format_24_ore = True if input("Doriți conversia în formatul de 24 de ore? (Da/Nu): ").lower() == "da" else False

    ore_minute, perioada = timp_input.split()
    ore, minute = map(int, ore_minute.split(":"))

    if format_24_ore:
        if perioada == "PM" and ore != 12:
            ore += 12
        elif perioada == "AM" and ore == 12:
            ore = 0

        timp_24_ore = f"{ore:02d}:{minute:02d}"
        print("Timpul convertit în formatul de 24 de ore:", timp_24_ore)
    else:
        if ore >= 12:
            perioada = "PM"
            if ore > 12:
                ore -= 12
        elif ore == 0:
            ore = 12
            perioada = "AM"
        else:
            perioada = "AM"

        timp_12_ore = f"{ore:02d}:{minute:02d} {perioada}"
        print("Timpul convertit în formatul de 12 ore:", timp_12_ore)
