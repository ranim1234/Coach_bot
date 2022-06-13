def prod_serializer(prod) -> dict:
    return {
        "id": str(prod["_id"]),
        "nom":prod["nom"],
        "clientele": prod["clientele"],
        "description": prod["description"],
        "taille_march": prod["taille_march"],
        "nb_concurrents": prod["nb_concurrents"],
        "prix_prod": prod["prix_prod"],
        "categorie": prod["categorie"],
        "entreprise": prod["entreprise"],
        "chiffre_affaire_annee": prod["chiffre_affaire_annee"],
        "benefice": prod["benefice"],
        "budget_comm": prod["budget_comm"],
        "budget_annee_prochaine": prod["budget_annee_prochaine"],


    }

def prods_serializer(prods) -> list:
    return [prod_serializer(prod) for prod in prods]