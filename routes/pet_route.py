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
    
    if all_pets:
    
        pets_formatados = [PetModel(**pet).model_dump() for pet in all_pets]
        
        pet_list = PetList(pets=pets_formatados).model_dump()
        
        return response.json(pet_list)
    else:
        return response.json({"Message": "Nenhum registro de pet encontrado"})
    

@PET_ROUTE.route('/get/pet/<pet_id>/', methods=['GET'])
async def get_one_pet(request: Request, pet_id):
    try:
        pet = collection.find_one({"_id": ObjectId(pet_id)})
        
        if pet:
            pet_instance = PetModel(**pet)
            pet_dict = pet_instance.model_dump()
            
            return response.json(pet_dict)
        else:
            return response.json({"Pet not found"}, status=404)  
        
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })
    

@PET_ROUTE.route('/create/pet/', methods=['GET','POST'])
async def create_pet(request: Request):
    try:
        pet = PetModel(**request.json)

        collection.insert_one(pet.model_dump())

        return response.json({"Message":"Registro adicionado", "Pet adicionado": pet.model_dump()})
    
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })
        

@PET_ROUTE.route('/update/pet/<pet_id>/', methods=['PUT', 'PATCH', 'GET'])
async def update_pet(request: Request, pet_id):
    try:   
        pet = collection.find_one({"_id": ObjectId(pet_id)})
        
        print(request.method)
        
        if pet:
            
            if request.method == 'PUT':
        
                pet_instance = PetModel(**request.json)
                pet_dict = pet_instance.model_dump()
                
                collection.update_one({"_id": ObjectId(pet_id)}, {"$set":  pet_dict})
            
            if request.method == 'PATCH':
                update_pet_instance = UpdatePetModel(**request.json)
                update_pet_dict = update_pet_instance.model_dump()
                
                collection.update_one({"_id": ObjectId(pet_id)}, {"$set":  update_pet_dict})
                
                pet = collection.find_one({"_id": ObjectId(pet_id)})
                
                pet_instance = PetModel(**pet)
                pet_dict = pet_instance.model_dump()
                
        
            return response.json({"Message":"Registro atualizado", "Pet atualizado": pet_dict})
        
        else:
            return response.json({"Pet not found"}, status=404)
        
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })

@PET_ROUTE.route('/delete/pet/<pet_id>/', methods=['GET', 'DELETE'])
async def delete_one_pet(request: Request, pet_id:str):
    pet = collection.find_one({"_id": ObjectId(pet_id)})
    
    if pet:
        collection.delete_one(pet)
        pet_dict = PetModel(**pet).model_dump()
        
        return response.json({"Message": "Pet deletado com sucesso", "Pet deletado": pet_dict})
    else:
        return response.json({"Petshop not found"}, status=404)