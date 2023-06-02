#Exercițiul 8: Convertor de timp
#Scrie un program care preia numărul de secunde ca intrare și îl convertește în ore, minute și secunde.
# Afișează timpul convertit.

secunde = int(input("Introdu numarul de secunde "))

ore = secunde // 3600
secunde_ramase = secunde % 3600
minute = secunde_ramase // 60
secunde_finale = secunde_ramase % 60


print(f"Numarul de ore este: {ore}, numarul de minute este {minute} si secundele sunt {secunde}")

