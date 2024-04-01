from bson import ObjectId
from pydantic import ValidationError
from sanic import Blueprint, Request, response

from conexao_db import db
from models import PetList, PetModel, UpdatePetModel

PET_ROUTE = Blueprint("pet")
collection = db['pet']


@PET_ROUTE.route('/pets/', methods=['GET'])
async def get_all_pet(request: Request):
    all_pets = collection.find()

    pets_dict = PetList(all_pets).model_dump()

    return response.json(pets_dict)


@PET_ROUTE.route('/pets/<pet_id:str>/', methods=['GET'])
async def get_one_pet(request: Request, pet_id: str):
    try:
        pet = collection.find_one({"_id": ObjectId(pet_id)})

        pet_dict = PetModel(**pet).model_dump() if pet else None

        return response.json(pet_dict)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/pets/', methods=['POST'])
async def create_pet(request: Request):
    try:
        pet = PetModel(**request.json).model_dump(exclude_none=True)

        collection.insert_one(pet)

        return response.json({"Message": "Registro adicionado", "Pet adicionado": PetModel(**pet).model_dump()}, status=201)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/pets/<pet_id:str>/', methods=['PUT'])
async def update_pet(request: Request, pet_id: str):
    try:
        update_pet = PetModel(**request.json).model_dump(exclude={'id'})

        update = collection.update_one({"_id": ObjectId(pet_id)}, {"$set": update_pet})

        if update.raw_result['updatedExisting'] is False:
            return response.json({"Message": "Pet not found"}, status=404)

        if update.modified_count == 1:

            pet_atualizado = collection.find_one({"_id": ObjectId(pet_id)})

            return response.json({"Message": "Registro atualizado", "Pet atualizado": PetModel(**pet_atualizado).model_dump()})

        if update.modified_count == 0:
            return response.json({"Message": "Nenhuma alteração foi feita no registro"})

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/pets/<pet_id:str>/', methods=['PATCH'])
async def update_pet_patch(request: Request, pet_id: str):
    try:
        update_pet = UpdatePetModel(**request.json).model_dump(exclude_none=True)

        update = collection.update_one({"_id": ObjectId(pet_id)}, {"$set":  update_pet})

        if update.raw_result['updatedExisting'] == False:
            return response.json({"Message": "Pet not found"}, status=404)

        if update.modified_count == 1:

            pet_atualizado = collection.find_one({"_id": ObjectId(pet_id)})

            return response.json({"Message": "Registro atualizado", "Pet atualizado": PetModel(**pet_atualizado).model_dump()})

        if update.modified_count == 0:
            return response.json({"Message": "Nenhuma alteração foi feita no registro"})

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/pets/<pet_id>/', methods=['DELETE'])
async def delete_one_pet(request: Request, pet_id: str):
    try:
        delecao = collection.delete_one({"_id": ObjectId(pet_id)})

        if delecao.deleted_count == 1:
            return response.text('', status=204)
        else:
            return response.json({"Message": "Pet not found"}, status=404)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })
