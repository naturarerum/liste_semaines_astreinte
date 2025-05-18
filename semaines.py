import locale
from datetime import date, timedelta


def generer_liste_semaines(debut, fin, gestionnaires, premier_gestionnaire=None):
    """ Produit une liste de semaines entre deux dates données
 Args :
    debut (date) : date de debut
    fin (date) : date de fin
    gestionnaires (list) : liste des gestionnaires en astreinte - nom et numéro de telephone

 Returns : liste_semaines : liste de semaines """

    locale.setlocale(category=locale.LC_ALL, locale="")  # Configuration pour le français

    liste_semaines = []
    date_courante = debut
    heure_debut = "8:00"
    gestionnaire_index = 0

    if premier_gestionnaire and premier_gestionnaire in gestionnaires:
        gestionnaire_index = gestionnaires.index(premier_gestionnaire)

    while date_courante < fin:
        debut_semaine = date_courante
        fin_semaine = debut_semaine + timedelta(days=7)
        gestionnaire_actuel = gestionnaires[gestionnaire_index % len(gestionnaires)]

        liste_semaines.append(
            f"Du {debut_semaine.day} {debut_semaine.strftime('%B')} {heure_debut} au {fin_semaine.day} {fin_semaine.strftime('%B')} {heure_debut} {gestionnaire_actuel}")
        date_courante = fin_semaine
        gestionnaire_index += 1

    return liste_semaines


if __name__ == "__main__":
    date_debut_str = input("Entrez la date de dÃ©but au format AAAA-MM-JJ : ")
    date_fin_str = input("Entrez la date de fin au format AAAA-MM-JJ : ")
    liste_gestionnaires_str = input( "Entrez les gestionnaires séparés par des virgules (ex: Olivier - 514-222-1234, Philippe - 418-111-1113) : ")
    gestionnaires = [g.strip() for g in liste_gestionnaires_str.split(',')]
    premier_gest_input = input("Gestionnaire qui commence la série (laisser vide pour le premier de la liste) : ")
    if not gestionnaires:
        print("Entrez une liste de gestionnaires")
    else :
        try:
            date_debut = date.fromisoformat(date_debut_str)
            date_fin = date.fromisoformat(date_fin_str)
            if date_debut > date_fin:
                print("La date de début doit être antérieure  a la date de fin.")
            else:
                semaines = generer_liste_semaines(date_debut, date_fin, gestionnaires, premier_gest_input.strip() or None)
            for semaine in semaines:
                print(semaine)
        except ValueError:
            print("Format de date invalide. Veuillez utiliser le format AAAA-MM-JJ.")
