'''
Scrie o listă comprehensivă care generează o listă a primelor litere ale fiecărui cuvânt dintr-un anumit enunț.
De exemplu, dacă enunțul este "Python este minunat", lista comprehensivă ar trebui să producă ['P', 'e', 'm'].
'''
user = input("Introdu un sir de caractere")
lista_comprehensive = [char[0] for char in user.split()]
print(lista_comprehensive)