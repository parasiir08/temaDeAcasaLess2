class Forma:
    def __init__(self, inner_color, border_color):
        self.__inner_color = inner_color
        self.__border_color = border_color

    def get_inner_color(self):
        return self.__inner_color

    def set_inner_color(self, new_color):
        self.__inner_color = new_color

    def get_border_color(self):
        return self.__border_color

    def set_border_color(self, new_color):
        self.__border_color = new_color


class Cerc(Forma):
    def __init__(self, inner_color, border_color, raza):
        super().__init__(inner_color, border_color)
        self.raza = raza

    def get_raza(self):
        return self.raza

    def set_raza(self, new_raza):
        self.raza = new_raza


class Dreptunghi(Forma):
    def __init__(self, inner_color, border_color, latime, lungime):
        super().__init__(inner_color, border_color)
        self.latime = latime
        self.lungime = lungime


class Patrat(Dreptunghi):
    def __init__(self, inner_color, border_color, latura):
        super().__init__(inner_color, border_color, latime=latura, lungime=latura)

    @property
    def latura(self):
        return self.latime

    @latura.setter
    def latura(self, new_latura):
        self.latime = new_latura
        self.lungime = new_latura


# Exemplu de utilizare
patrat = Patrat(inner_color="albastru", border_color="verde", latura=5)
print("Culoarea interioară a pătratului:", patrat.get_inner_color())
print("Culoarea marginii a pătratului:", patrat.get_border_color())
print("Latura pătratului:", patrat.latura)  # sau patrat.get_latura()

patrat.latura = 8
print("Latura pătratului după modificare:", patrat.latura)
print("Lungimea pătratului după modificare:", patrat.lungime)
