import datetime

class Human:
    def __init__(self, nume, prenume, data_nasterii):
        self.nume = nume
        self.prenume = prenume
        self.data_nasterii = data_nasterii

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def varsta(self):
        today = datetime.date.today()
        birth_date = self.data_nasterii
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def __str__(self):
        return f"{self.nume_complet()}, vârsta {self.varsta()}"

# Exemplu de utilizare
if __name__ == "__main__":
    data_nasterii_marius = datetime.date(1999, 5, 15)
    marius = Human("Marius", "Tricolici", data_nasterii_marius)
    print(marius)  # Va afișa: Marius Tricolici, vârsta 24
