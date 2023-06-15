'''
Scrie o listă comprehensivă care generează o listă a literelor majuscule dintr-un anumit șir de caractere.
De exemplu, dacă șirul de caractere este "Salut Lume", lista comprehensivă ar trebui să producă ['S', 'L'].
'''

user = input("Introdu un sir de caractere")
lista_comprehensive = [char for char in user if char.isupper()]
print(lista_comprehensive)