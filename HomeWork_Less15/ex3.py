import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return dice1, dice2, total

def display_dice_roll(dice1, dice2, total):
    print(f"Zarul 1: {dice1}")
    print(f"Zarul 2: {dice2}")
    print(f"Total: {total}")

# Exemplu de utilizare
choice = input("Apăsați Enter pentru a arunca zarurile sau 'q' pentru a ieși: ")

while choice != "q":
    dice1, dice2, total = roll_dice()
    display_dice_roll(dice1, dice2, total)
    choice = input("Apăsați Enter pentru a arunca zarurile sau 'q' pentru a ieși: ")
