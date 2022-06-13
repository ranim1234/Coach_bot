import asyncio
from Entreprise.models.entreprise_model import Entreprise
from config.database import collection_name
from mongo.populate import populate_object, populate_array


def entreprise_serializer(entr) -> dict:
    return {
        "id": str(entr["_id"]),
        "nom": entr["nom"],
        "secteur_activite": entr["secteur_activite"],
        "annee_creation": entr["annee_creation"],
        "nb_prod": entr["nb_prod"],
        "chiffre_affaire": entr["chiffre_affaire"],
        "pays": entr["pays"],
        "region": entr["region"],
        "produit": entr["produit"],

    }

def entreprises_serializer(entrs) -> list:
    return [entreprise_serializer(entr) for entr in entrs]

#async def insert_product(entreprise:Entreprise):

    #document=collection_name.find_one({"entreprise": entreprise.nom}, {
      #  "$set": dict(prod)
    #})
    #entreprise1=Entreprise(**document)
    #entreprise.produit=entreprise1.produit

    #values = await asyncio.gather(
       # populate_object(collection_name["entreprise"], collection_name),
       # populate_array(mp.medicament, app.db.meds, "key"),

   # )
   # entreprise.produit=values
    #return entreprise