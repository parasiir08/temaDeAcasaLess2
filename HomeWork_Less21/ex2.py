import datetime

class Pet:
    def __init__(self, nume1, tip, mincare_preferata):
        self.nume1 = nume1
        self.tip = tip
        self.mincare_preferata = mincare_preferata

    def reprezentare_pet(self):
        return f"{self.tip} numită {self.nume1}, care iubește {self.mincare_preferata}"

class HumanWithPet:
    def __init__(self, nume2, prenume, data_nasterii, pets):
        self.nume2 = nume2
        self.prenume = prenume
        self.data_nasterii = data_nasterii
        self.pets = pets

    def nume_complet(self):
        return f"{self.nume2} {self.prenume}"

    def varsta(self):
        today = datetime.date.today()
        birth_date = self.data_nasterii
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def __str__(self):
        pets_str = "\n".join([pet.reprezentare_pet() for pet in self.pets])
        return f"{self.nume_complet()}, vârsta {self.varsta()}, cu animalele de companie:\n{pets_str}"

    def adaugare_pets(self):
        pets = []
        for i in range(nr_animale):
            tip = input(f"Introduceți tipul animalului {i + 1}: ")
            nume1 = input(f"Introduceți numele animalului {i + 1}: ")
            mincare_preferata = input(f"Introduceți mincarea preferată a animalului {i + 1}: ")
            pet = Pet(nume1, tip, mincare_preferata)
            pets.append(pet)

if __name__ == "__main__":
    nume2 = input("Introdu numele persoanei: ")
    prenume = input("Introdu prenumele persoanei: ")
    data_nasterii_str = input("Introduceți data nașterii în formatul YYYY-MM-DD: ")
    data_nasterii_marius = datetime.datetime.strptime(data_nasterii_str, "%Y-%m-%d").date()
    nr_animale = int(input("Introduceți numărul de animale de companie pe care le aveți: "))



    hwp = HumanWithPet(nume2, prenume, data_nasterii_marius, adaugare_pets.pets)
    print(hwp)

