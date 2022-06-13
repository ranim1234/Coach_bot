import asyncio
from fastapi import APIRouter
from Entreprise.models.entreprise_model import Entreprise
from Entreprise.schemas.entreprise_schema import entreprises_serializer

from Produit.models.produit_model import produit
from config.database import collection_name1, collection_name

from bson import ObjectId

from mongo.populate import populate_object

entreprise_api_router = APIRouter()

# retrieve
@entreprise_api_router.get("/entreprise")
async def get_entrs():
    entrs = entreprises_serializer(collection_name1.find())
    return entrs

@entreprise_api_router.get("/entreprise/{id}")
async def get_entr(id: str):
    return entreprises_serializer(collection_name1.find_one({"_id": ObjectId(id)}))


# post
@entreprise_api_router.post("/entreprise")
async def create_entr(entr: Entreprise):
    #values=['haha','kiki']
    var=[]
    i=0
    while i<=100:
        values = collection_name.find({"entreprise": entr.nom})
        i=i+1
    for value in values:
        var.append(value['nom'])
    entr.produit=var
    _id = collection_name1.insert_one(dict(entr))
    return entreprises_serializer(collection_name1.find({"_id": _id.inserted_id}))


# update
@entreprise_api_router.put("/entreprise/{id}")
async def update_entr(id: str, entr: Entreprise):
    collection_name1.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(entr)
    })
    return entreprises_serializer(collection_name1.find({"_id": ObjectId(id)}))

# delete
@entreprise_api_router.delete("/entreprise/{id}")
async def delete_entr(id: str):
    collection_name1.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}