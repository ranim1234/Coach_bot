from pydantic import BaseModel
from bson.objectid import ObjectId

class produit(BaseModel):
    nom:str
    clientele:str
    description:str
    taille_march:float
    nb_concurrents:int
    prix_prod:float
    categorie:str
    chiffre_affaire_annee:float
    benefice:float
    budget_comm:float
    budget_annee_prochaine:float
    entreprise:str