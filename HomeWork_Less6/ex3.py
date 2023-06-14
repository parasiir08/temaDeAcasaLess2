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
pass_length = int(input('Pass length'))

password1 = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(password))
    password1 += password[letter_index]
print(f" Parola este {password1}")