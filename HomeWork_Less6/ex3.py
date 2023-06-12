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
pass_length = int(input('Pass length'))

password = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(all_letters))
    all_numbers1 = random.randrange(0, len(all_numbers))
    rand_symbols = random.randrange(0, len(all_symbols))

    password += all_letters[letter_index] + all_symbols[rand_symbols] + all_numbers[all_numbers1]

    print(password)