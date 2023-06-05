"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""
subsir = input("Introdu o propozitie sau un subsir ")
inlocuire = input("Introdu un subsir de caractere de inlocuire")

process_inlocuire = subsir.replace(subsir, inlocuire)
print(process_inlocuire)

