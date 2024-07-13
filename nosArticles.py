import json

nosArticles = []

def validation_de_nom_articles(nomArticle):
    if any(char.isdigit() for char in nomArticle):
        print("Erreur de saisi ! votre nom d'article ne peut contenir de chiffres.")
        return False
    return True

def validation_prix_article(prixArticle):
    try:
        float(prixArticle)
        return True
    except ValueError:
        print("Erreur ! prix de l'article doit être un nombre .")
        return False

def validation_qte_article(quantite_article):
    if quantite_article.isdigit():
        return True
    else:
        print("Erreur ! la quantité de l'article saisi doit être un nombre entier ! saisissez a nouveau !.")
        return False

def ajouter_produit():
    print("=== === === ENTREZ LES INFORMATIONS DE L'ARTICLE AVANT DE L'AJOUTER === === ===")
    id_produit = len( nosArticles) + 1
    while True:
        nom = input("Entrez le nom de l'article: ")
        if validation_de_nom_articles(nom):
            break

    # Vérifier si le produit existe déjà
    for produit in  nosArticles:
        if produit['nom'].lower() == nom.lower():
            print("Erreur ! Le produit saisi existe déjà ! veilliez saisir a nouveau.")
            return

    while True:
        prix = input(" Saisir le prix du produit: ")
        if validation_prix_article(prix):
            prix = float(prix)
            break

    while True:
        quantite = input("Veilliez entrer la quantité du produit souhaiter: ")
        if validation_qte_article(quantite):
            quantite = int(quantite)
            break

    produit = {'id_produit': id_produit, 'nom': nom, 'prix': prix, 'quantite': quantite}
    nosArticles.append(produit)

    sauvegarder_produits()

    print("**** ****** ***** PRODUIT AJOUTE AVEC SUCCES! **** ***** *****")

def affichage_produits():
    if not  nosArticles:
        print("*** *** *** AUCUN PRODUIT N'EST DISPONIBLE DANS NOTRE MAGASIN POUR LE MOMENT. *** ***")
    else:
        print("=== === === VOICI LES PRODUITS DISPONIBLES DANS LE MAGASIN === === ===")
        for produit in  nosArticles:
            print(f"id_produit : {produit['id_produit']}, Nom: {produit['nom']}, Prix: {produit['prix']}, Quantité: {produit['quantite']}")

def rechercher_produits():
    print("=== === === ENTREZ LES INFORMATIONS POUR RECHERCHER UN ARTICLE === === ===")
    choix = input("Voulez-vous faire une rechercher par nom ou par ID? (nom/id): ").lower()
    produit_trouver = None

    if choix == "nom":
        nom = input("Veilliez entrez le nom du produit à rechercher: ")
        for produit in  nosArticles:
            if produit['nom'].lower() == nom.lower():
                produit_trouver = produit
                break
    elif choix == "id":
        id_produit = input("Veilliez entrez l'ID du produit à rechercher: ")
        if id_produit.isdigit():
            id_produit = int(id_produit)
            for produit in  nosArticles:
                if produit['id_produit'] == id_produit:
                    produit_trouver = produit
                    break

    if produit_trouver:
        print(f"Voici le produit recherché : id_produit: {produit_trouver['id_produit']}, Nom: {produit_trouver['nom']}, Prix: {produit_trouver['prix']}, Quantité: {produit_trouver['quantite']}")
        choix_de_modification = input("Voulez-vous modifier ce produit ? (oui/non): ").lower()
        if choix_de_modification == "oui":
            modification_du_produit(produit_trouver['id_produit'])
            print("*** *** *** LE PRODUIT A ETE MODIFIÉ AVEC SUCCÈS *** *** ***")
        choix_de_suppression = input("Voulez-vous supprimer ce produit !? (oui/non): ").lower()
        if choix_de_suppression == "oui":
            suppression_produit(produit_trouver['id_produit'])
            print("*** *** *** PRODUIT SUPPRIMÉ AVEC SUCCÈS *** *** ***")
    else:
        print("*** *** *** LE PRODUIT RECHERCHÉ EST INTROUVABLE. *** *** ***")

def modification_du_produit(id_produit):
    for produit in  nosArticles:
        if produit['id_produit'] == id_produit:
            while True:
                nom = input(f"Entrez le nouveau nom du produit (actuel: {produit['nom']}): ")
                if validation_de_nom_articles(nom):
                    produit['nom'] = nom
                    break

            while True:
                prix = input(f"Entrez le nouveau prix du produit (actuel: {produit['prix']}): ")
                if validation_prix_article(prix):
                    produit['prix'] = float(prix)
                    break

            while True:
                quantite = input(f"Entrez la nouvelle quantité du produit (actuelle: {produit['quantite']}): ")
                if validation_qte_article(quantite):
                    produit['quantite'] = int(quantite)
                    break

            sauvegarder_produits()
            break

def suppression_produit(id_produit):
    global  nosArticles
    nosArticles = [produit for produit in  nosArticles if produit['id_produit'] != id_produit]
    sauvegarder_produits()

def charger_produits():
    global  nosArticles
    try:
        with open(' nosArticles.json', 'r') as f:
             nosArticles = json.load(f)
    except FileNotFoundError:
         nosArticles = []

def mettre_a_jour_stock(produit_nom, quantite_vendue):
    for produit in  nosArticles:
        if produit['nom'].lower() == produit_nom.lower():
            produit['quantite'] -= quantite_vendue
            break

def verifier_stock(produit_nom, quantite_vendue):
    for produit in  nosArticles:
        if produit['nom'].lower() == produit_nom.lower():
            return produit['quantite'] >= quantite_vendue
    return False

def sauvegarder_produits():
    with open(' nosArticles.json', 'w') as f:
        json.dump( nosArticles, f)

# Charger les  nosArticles au démarrage
charger_produits()
