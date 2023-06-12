'''
Scrieți un program care primește două șiruri de caractere ca intrare
și verifică dacă acestea sunt anagrame
(adică un cuvânt poate fi format prin rearanjarea literelor altui cuvânt).
'''

sirul1 = input("Introdu primul sir ")
sirul2 = input("Introdu al 2-lea sir ")

if (sorted(sirul1)) == (sorted(sirul2)):
    print("Sirurile sunt anagrame")
else:
    print("Sirurile nu sunt anagrame")
