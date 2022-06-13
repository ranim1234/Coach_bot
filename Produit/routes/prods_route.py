from fastapi import APIRouter
from Entreprise.models.entreprise_model import Entreprise
from Entreprise.schemas.entreprise_schema import entreprises_serializer

from Produit.models.produit_model import produit
from config.database import collection_name

from Produit.schemas.produit_schema import prods_serializer
from bson import ObjectId

prod_api_router = APIRouter()

# retrieve
@prod_api_router.get("/")
async def get_prods():
    prods = prods_serializer(collection_name.find())
    return prods

@prod_api_router.get("/{id}")
async def get_prod(id: str):
    return prods_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@prod_api_router.post("/")
async def create_prod(prod: produit):
    _id = collection_name.insert_one(dict(prod))
    return prods_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@prod_api_router.put("/{id}")
async def update_prod(id: str, prod: produit):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(prod)
    })
    return prods_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@prod_api_router.delete("/{id}")
async def delete_prod(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}


