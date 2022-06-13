from fastapi import FastAPI
from Produit.routes.prods_route import prod_api_router
from Entreprise.routes.entreprise_route import entreprise_api_router


app = FastAPI()

app.include_router(prod_api_router)

app.include_router(entreprise_api_router)



