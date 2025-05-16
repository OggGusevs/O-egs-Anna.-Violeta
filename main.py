from analizators import LaikaAnalizators
from laika_dati import LaikaDiena

def main():
    analizators = LaikaAnalizators("Ventspils")

    dati = [
        LaikaDiena("2025-05-10", 15, 2.5, 5),
        LaikaDiena("2025-05-11", 18, 0.0, 3),
        LaikaDiena("2025-05-12", 12, 5.0, 6),
        LaikaDiena("2025-05-13", 20, 1.0, 4),
        LaikaDiena("2025-05-14", 17, 5.0, 2)
    ]

    for diena in dati:
        analizators.pievienot_dienu(diena)

    print("Laika prognoze Ventspilī:")
    analizators.paradit_visas_dienas()
    print()
    analizators.silta_diena(16)
    print()
    analizators.lietainakas_dienas()
    print()
    print(f"Vidējā temperatūra: {analizators.vid_temps():.1f}°C")

if __name__ == "__main__":
    main()