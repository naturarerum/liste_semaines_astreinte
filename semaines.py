import locale
from datetime import date, timedelta


def generer_liste_semaines(debut, fin):
    """ Produit une liste de semaines entre deux dates données
 Args :
    debut (date) : date de debut
    fin (date) : date de fin

 Returns : liste_semaines : liste de semaines """

    locale.setlocale(category=locale.LC_ALL, locale="")  # Configuration pour le français

    liste_semaines = []
    date_courante = debut
    heure_debut = "8:00"
    gest = premier_gest
    gest1 = "Olivier - 514-222-1234"
    gest2 = "Philippe - 418-111-1113"
    change_gest = False

    while date_courante < fin:
        debut_semaine = date_courante
        fin_semaine = debut_semaine + timedelta(days=7)


        if change_gest and gest == "Olivier - 514-222-1234":
            gest = "Philippe - 418-111-1113"
        elif change_gest and gest == "Philippe - 418-111-1113":
            gest = "Olivier - 514-222-1234"

        liste_semaines.append(
            f"Du {debut_semaine.day} {debut_semaine.strftime('%B')} {heure_debut} au {fin_semaine.day} {fin_semaine.strftime('%B')} {heure_debut} {gest}")
        date_courante = fin_semaine
        change_gest = True

    return liste_semaines


if __name__ == "__main__":
    date_debut_str = input("Entrez la date de dÃ©but au format AAAA-MM-JJ : ")
    date_fin_str = input("Entrez la date de fin au format AAAA-MM-JJ : ")
    premier_gest = input("gestionnaire qui commence la série (gest1 = Olivier, gest2 = Philippe : ")
    try:
        date_debut = date.fromisoformat(date_debut_str)
        date_fin = date.fromisoformat(date_fin_str)
        if date_debut > date_fin:
            print("La date de début doit être antérieure  a la date de fin.")
        else:
            semaines = generer_liste_semaines(date_debut, date_fin)
        for semaine in semaines:
            print(semaine)
    except ValueError:
        print("Format de date invalide. Veuillez utiliser le format AAAA-MM-JJ.")
