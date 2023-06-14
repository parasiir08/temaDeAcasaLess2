"""
Improve the password generator
Inbunatatiti acest generator de parole, astfel in cat sa fie posibil sa genereze parole ce contin atat litere,
 cat si cifre si caractere speciale.
"""
import string
import random

all_letters = list(string.ascii_letters)
all_symbols = list(string.punctuation)
all_numbers = list(string.digits)
password = all_letters + all_symbols + all_numbers
pass_length = int(input('Lungimea parolei: '))

password1 = ''
for _ in range(pass_length):
    character = random.choice(password)
    password1 += character

print(f"Parola generată este: {password1}")
