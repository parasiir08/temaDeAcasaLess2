'''
Scrieți o funcție Python numită is_palindrome care verifică dacă un șir de caractere dat este un palindrom.
Funcția ar trebui să primească un singur argument: text (șir de caractere) care reprezintă textul de verificat.
Funcția ar trebui să returneze o valoare booleană care indică dacă textul este un palindrom.

Sugestie: Un palindrom este un cuvânt, o frază, un număr sau o altă secvență de caractere
care se citește la fel înainte și înapoi, fără a ține cont de spații, semne de punctuație și capitalizare.

Scrieți un program care utilizează funcția is_palindrome pentru a face următoarele:

Solicitați utilizatorului să introducă un text.
Apelați funcția is_palindrome cu valoarea introdusă.
Afișați dacă textul este un palindrom sau nu.
'''
def is_palindrome(text:str):

    reversare = text[::-1]
    if (reversare == text):
        print("Este un palindrom")
    else:
        print("Nu este un palindrom")

cuvint = input("Introdu caracterele pentru a verifica daca sunt palindrome ")
print(is_palindrome(cuvint))