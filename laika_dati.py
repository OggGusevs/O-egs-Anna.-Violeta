class LaikaDiena:
    id_counter = 1

    def __init__(self, datums, temperatura, nokrisni, vejs):
        self.id = LaikaDiena.id_counter
        LaikaDiena.id_counter += 1
        self.datums = datums
        self.temperatura = temperatura
        self.nokrisni = nokrisni
        self.vejs = vejs

    def __str__(self):
        return f"{self.id}. {self.datums}: {self.temperatura}°C, Nokrišņi: {self.nokrisni} mm, Vējš: {self.vejs} m/s"