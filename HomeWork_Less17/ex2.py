import time
from datetime import timedelta, datetime

def calc_days_until_event():
    while True:
        try:
            timpul = input("Introdu timpul pana la un eveniment in urmatorul format (dd/mm/YYYY HH:MM): ")
            name_event = input("Care este evenimentul pe care il astepti? ")
            event_datetime = datetime.strptime(timpul, "%d/%m/%Y %H:%M")
            current_datetime = datetime.now()
            one_year = timedelta(days=365)
            timp_ramas= event_datetime.timestamp() - current_datetime.timestamp()

            if event_datetime > current_datetime + one_year:
                raise ValueError("Data este cu mai mult de un an inainte.")

            break  # Dacă data este validă, ieșim din bucla while
        except ValueError as e:
            print("Eroare:", str(e))
            print("Vă rugăm să introduceți o dată validă.\n")

    days_until_event = (event_datetime - current_datetime).days

    while timp_ramas > 0:
        zile = timp_ramas // (24 * 3600)
        timp_ramas %= (24 * 3600)
        ore = timp_ramas // 3600
        timp_ramas %= 3600
        minute = timp_ramas // 60
        secunde = timp_ramas % 60

        print(f"Numarul de zile pana la {name_event}: {days_until_event} zile.")
        print(f"Timp ramas: {zile} zile, {ore} ore, {minute} minute, {secunde:.2f} secunde.")
        time.sleep(1)

        current_datetime = datetime.now()
        timp_ramas = event_datetime.timestamp() - current_datetime.timestamp()
        days_until_event = (event_datetime - current_datetime).days

calc_days_until_event()
