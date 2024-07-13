from nosArticles import charger_produits
from vente import charger_ventes

def charger_donnees():
    charger_produits()
    charger_ventes()

    print("Données chargées avec succès.")
