import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def display_dice_roll(dice_values, total):
    print("Zarurile: ", end="")
    for dice in dice_values:
        print(f"{dice} ", end="")
    print(f"\nTotal: {total}")

# Exemplu de utilizare
num_sides = int(input("Introduceți numărul de laturi al zarului: "))
num_dice = int(input("Introduceți numărul de zaruri: "))

choice = ""

while choice != "STOP":
    dice_values = [roll_dice(num_sides) for _ in range(num_dice)]
    total = sum(dice_values)
    display_dice_roll(dice_values, total)
    choice = input("Apăsați Enter pentru a arunca din nou sau introduceți 'STOP' pentru a opri: ")
