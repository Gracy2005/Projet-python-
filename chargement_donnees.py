import json

def charger_donnees(fichier):
    try:
        with open(fichier, 'r') as f:
            data = json.load(f)
            global produits, vente
            produits = data['produits']
            vente = data['ventes']
            print("Données chargées avec succès!")
    except FileNotFoundError:
        print("Fichier non trouvé.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")
