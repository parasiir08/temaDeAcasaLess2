'''
Creează o funcție care primește o șir de caractere ca intrare și verifică dacă este un palindrom.
Gestionează eroarea de tip ValueError dacă se furnizează un șir de caractere gol.
Task:

Definește o funcție care acceptă un singur parametru.
Verifică dacă șirul de caractere de intrare este gol folosind o instrucțiune if.
Dacă șirul este gol, generează o eroare de tip ValueError cu un mesaj de eroare adecvat.
Dacă șirul nu este gol, compară-l cu oglinditul său și returnează True dacă sunt egale (un palindrom) sau False în caz contrar.
'''

def is_palindrome(text: str):
    try:
        if not text.strip():
            raise ValueError("Ai introdus un șir gol")
    except ValueError as ex:
        print(ex)
        return

    reversare = text[::-1]

    if reversare == text:
        print("Este un palindrom")
    else:
        print("Nu este un palindrom")

cuvant = input("Introdu caracterele pentru a verifica dacă este palindrom: ")
is_palindrome(cuvant)
