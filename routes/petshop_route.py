from bson import ObjectId
from pydantic import ValidationError
from sanic import Blueprint, Request, response

from conexao_db import db
from models import PetshopList, PetshopModel, UpdatePetshopModel

PETSHOP_ROUTE = Blueprint("petshop")
collection = db['petshop']


@PETSHOP_ROUTE.route('/petshops/', methods=['GET'])
async def get_all_petshop(request: Request):
    all_petshops = collection.find()

    petshops_dict = PetshopList(all_petshops).model_dump()

    return response.json(petshops_dict)


@PETSHOP_ROUTE.route('/petshops/<petshop_id:str>/', methods=['GET'])
async def get_one_petshop(request: Request, petshop_id: str):
    try:
        petshop = collection.find_one({"_id": ObjectId(petshop_id)})

        petshop_dict = PetshopModel(**petshop).model_dump() if petshop else None

        return response.json(petshop_dict)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PETSHOP_ROUTE.route('/petshops/', methods=['POST'])
async def create_petshop(request: Request):
    try:
        petshop = PetshopModel(**request.json).model_dump(exclude_none=True)

        collection.insert_one(petshop)

        return response.json({"Message": "Registro adicionado", "Petshop adicionado": PetshopModel(**petshop).model_dump()}, status=201)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PETSHOP_ROUTE.route('/petshops/<petshop_id:str>/', methods=['PUT'])
async def update_petshop(request: Request, petshop_id: str):
    try:
        update_petshop = UpdatePetshopModel(**request.json).model_dump(exclude={'id'})

        update = collection.update_one({"_id": ObjectId(petshop_id)}, {"$set": update_petshop})

        if update.raw_result['updatedExisting'] == False:
            return response.json({"Message": "Petshop not found"}, status=404)

        if update.modified_count == 1:
            petshop_atualizado = collection.find_one({"_id": ObjectId(petshop_id)})

            return response.json({"Message": "Registro atualizado", "Petshop atualizado": PetshopModel(**petshop_atualizado).model_dump()})

        if update.modified_count == 0:
            return response.json({"Message": "Nenhuma alteração foi feita no registro"})
    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PETSHOP_ROUTE.route('/petshops/<petshop_id:str>/', methods=['PATCH'])
async def update_petshop_patch(request: Request, petshop_id: str):
    try:
        update_petshop = UpdatePetshopModel(**request.json).model_dump(exclude_none=True)

        update = collection.update_one({"_id": ObjectId(petshop_id)}, {"$set": update_petshop})

        if update.raw_result['updatedExisting'] == False:
            return response.json({"Message": "Petshop not found"}, status=404)

        if update.modified_count == 1:

            petshop_atualizado = collection.find_one({"_id": ObjectId(petshop_id)})

            return response.json({"Message": "Registro atualizado", "Pet atualizado": PetshopModel(**petshop_atualizado).model_dump()})

        if update.modified_count == 0:
            return response.json({"Message": "Nenhuma alteração foi feita no registro"})

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PETSHOP_ROUTE.route('/petshops/<petshop_id:str>/', methods=['DELETE'])
async def delete_one_petshop(request: Request, petshop_id: str):
    petshop = collection.find_one({"_id": ObjectId(petshop_id)})

    if petshop:
        collection.delete_one(petshop)

        return response.text('', status=204)
    else:
        return response.json({"Message": "Petshop not found"}, status=404)
