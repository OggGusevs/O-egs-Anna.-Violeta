from laika_dati import LaikaDiena

class LaikaAnalizators:
    def __init__(self, pilseta):
        self.pilseta = pilseta
        self.dienas = []

    def pievienot_dienu(self, diena):
        self.dienas.append(diena)

    def paradit_visas_dienas(self):
        for diena in self.dienas:
            print(diena)

    def silta_diena(self, slieksnis):
        for diena in self.dienas:
            if diena.temperatura > slieksnis:
                print(diena)

    def lietainakas_dienas(self):
        max_nokrisni = max(self.dienas, key=lambda d: d.nokrisni).nokrisni
        for diena in self.dienas:
            if diena.nokrisni == max_nokrisni:
                print(diena)

    def vid_temps(self):
        if not self.dienas:
            return 0
        return sum([d.temperatura for d in self.dienas]) / len(self.dienas)