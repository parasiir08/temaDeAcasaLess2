'''
Creati un program python cu ajutorul careia vor fi gasite toate elementele dintr-o lista de string-uri care sunt palindroame.
Avand lista ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] rezultatul va fi ['php', 'aaa'].

Note: Puteti folosi functia filter pentru a filtra elementele unei colectii.
'''


all_list_elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

#for el in all_list_elements:
#    if el == el[::-1]:
#       print(f"Cuvintele palindrome sunt {el}")

def palindrom():
    return [el == el[::-1] for el in all_list_elements]

b = list(filter(palindrom(), all_list_elements))
print(b)
