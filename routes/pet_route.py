from bson import ObjectId
from pydantic import ValidationError
from sanic import Blueprint, Request, json, response
from conexao_db import db
from models import PetList, PetModel, UpdatePetModel

PET_ROUTE = Blueprint("pet")
collection = db['pet']


@PET_ROUTE.route('/get/all/pet/', methods=['GET'])
async def get_all_pet(request: Request):
    all_pets = collection.find()
    return response.json(
        PetList(root=all_pets).model_dump()
    )


@PET_ROUTE.route('/get/pet/<pet_id>/', methods=['GET'])
async def get_one_pet(request: Request, pet_id):
    try:
        pet = collection.find_one({"_id": ObjectId(pet_id)})

        return response.json(PetModel(**pet).model_dump() if pet else None)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/create/pet/', methods=['GET', 'POST'])
async def create_pet(request: Request):
    try:
        pet = PetModel(**request.json).model_dump()
        collection.insert_one(pet)

        return response.json({"Message": "Registro adicionado", "Pet adicionado": PetModel(**pet).model_dump()})

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/update/pet/<pet_id>/', methods=['PUT', 'PATCH', 'GET'])
async def update_pet(request: Request, pet_id):
    try:
        pet = collection.find_one({"_id": ObjectId(pet_id)})

        if pet:

            if request.method == 'PUT':

                pet_instance = PetModel(**request.json)
                pet_dict = pet_instance.model_dump()

                collection.update_one(
                    {"_id": ObjectId(pet_id)}, {"$set":  pet_dict})

            if request.method == 'PATCH':
                update_pet_instance = UpdatePetModel(**request.json)
                update_pet_dict = update_pet_instance.model_dump()

                collection.update_one({"_id": ObjectId(pet_id)}, {
                                      "$set":  update_pet_dict})

                pet = collection.find_one({"_id": ObjectId(pet_id)})

                pet_instance = PetModel(**pet)
                pet_dict = pet_instance.model_dump()

            return response.json({"Message": "Registro atualizado", "Pet atualizado": pet_dict})

        else:
            return response.json({"Pet not found"}, status=404)

    except ValidationError as e:
        erros = e.errors()

        return response.json({"Description": erros[0]["type"],
                              "Message error": erros[0]['msg'],
                              })


@PET_ROUTE.route('/delete/pet/<pet_id>/', methods=['GET', 'DELETE'])
async def delete_one_pet(request: Request, pet_id: str):
    collection.delete_one({"_id": ObjectId(pet_id)})
    return response.json(status=204)
