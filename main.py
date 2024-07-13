from nosArticles import *
from vente import *
from sauvegarde import *


def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit") 
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Quitter")
    return input("Choisissez une option: ")

def main():
    #charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '1':
           ajouter_produit()
        elif choix == '2':
            affichage_produits()
        elif choix == '3':
            rechercher_produits()
        elif choix == '4':
           enregistrer_vente()
        elif choix == '5':
           afficher_ventes()
        elif choix == '6':
          ventes_par_client()
        elif choix == '7':
           # generer_rapport_ventes()
           print("generer_rapport_ventes")
        elif choix == '8':
            #charger_donnees()
            print("charger_donnees")
        elif choix == '9':
            print("=== === === MERCI!!!! DE VISITER NOTRE MAISON")
        else:
            print(" *=*=*=*=*=* CHOIX INVALIDE, VEUILLEZ REESSAYER *=*=*=*=*=* ")

if __name__ == "__main__":
    main() 