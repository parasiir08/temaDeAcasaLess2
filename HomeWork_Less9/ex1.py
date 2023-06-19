'''
Creați două liste care vor reprezenta numele participanților la două evenimente. Transformați-le apoi în seturi.

Utilizați operațiile cu seturi și afișați rezultatele:

câți participanți au fost prezenți la ambele evenimente
câți participanți au fost prezenți doar la primul eveniment
câți participanți au fost prezenți doar la al doilea eveniment
'''

eveniment1 = ("Andrei","Valera","Grisha")
eveniment2 = ("Anton","Ion","Teseus")

my_set1 = set(eveniment1)
my_set2 = set(eveniment2)
print(len(my_set1.union(my_set2)),
      len(my_set1),
      len(my_set2)
      )





