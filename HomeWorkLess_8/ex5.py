'''
Scrie o listă comprehensivă care generează o listă a lungimilor cuvintelor dintr-un anumit enunț.
De exemplu, dacă enunțul este
"Salut lume, cum te simți?", lista comprehensivă ar trebui să producă [5, 5, 3, 3, 4].
'''

enunt = input("Scrie un enunt").split(" ")
lista_comprehensive = [len(char) for char in enunt]
print(lista_comprehensive)