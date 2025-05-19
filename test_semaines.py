from datetime import date

from semaines import generer_liste_semaines


def test_periode_normale():
    debut = date(2025, 6, 2)
    fin = date(2025, 6, 16)
    gestionnaires = ["Gestionnaire A", "Gestionnaire B"]
    resultat = generer_liste_semaines(debut, fin, gestionnaires)
    assert len(resultat) == 2
    assert "Gestionnaire A" in resultat[0]
    assert "Gestionnaire B" in resultat[1]


def test_alternance_gestionnaires():
    debut = date(2025, 6, 2)
    fin = date(2025, 6, 23)
    gestionnaires = ["toto", "titi", "tutu"]
    resultat = generer_liste_semaines(debut, fin, gestionnaires)
    assert len(resultat) == 3
    assert "toto" in resultat[0]
    assert "titi" in resultat[1]
    assert "tutu" in resultat[2]

def test_erreur_format_date():
    debut = date(25, 6, 2)
    fin = date(2025, 6, 23)
    gestionnaires = ["toto", "titi", "tutu"]
    resultat = generer_liste_semaines(debut, fin, gestionnaires)
    assert AssertionError

