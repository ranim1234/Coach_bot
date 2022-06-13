from pip import List
from pydantic import BaseModel
from Produit.models.produit_model import produit

class Entreprise(BaseModel):
    nom:str
    secteur_activite:str
    annee_creation:float
    nb_prod:float
    chiffre_affaire:float
    pays:str
    region:str
    produit:List[str]=['']




