class ListăNumere(list):
    def __init__(self, *args):
        super().__init__()
        self._validate_and_extend(args)

    def append(self, value):
        if self._is_valid_number(value):
            super().append(value)
        else:
            raise ValueError("Valoarea trebuie să fie numerica (int sau float).")

    def extend(self, iterable):
        validated_values = [value for value in iterable if self._is_valid_number(value)]
        super().extend(validated_values)

    def _is_valid_number(self, value):
        return isinstance(value, (int, float))

    def _validate_and_extend(self, values):
        validated_values = [value for value in values if self._is_valid_number(value)]
        super().extend(validated_values)

    def get_sum(self):
        return sum(self)

    def get_average(self):
        if not self:
            return 0
        return sum(self) / len(self)


# Exemplu de utilizare
numere = ListăNumere([1, 2, 3, 4, 5, 6, 7, 8])
numere.append(9)
numere.extend([10, "invalid", 11, 12.5])

print("Listă de numere:", numere)
print("Suma numerelor:", numere.get_sum())
print("Media numerelor:", numere.get_average())
