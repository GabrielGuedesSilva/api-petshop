from bson import ObjectId
from pydantic import ValidationError
from sanic import Blueprint, Request, response

from conexao_db import db
from models import PetshopList, PetshopModel, UpdatePetshopModel

PETSHOP_ROUTE = Blueprint("petshop")
collection = db['petshop']


@PETSHOP_ROUTE.route('/get/all/petshop/', methods=['GET'])
async def get_all_petshop(request: Request):
    all_petshops = collection.find()
    
    if all_petshops:
        petshops_formatados = [PetshopModel(**petshop).model_dump() for petshop in all_petshops]
        
        petshop_list = PetshopList(petshops=petshops_formatados).model_dump()

        return response.json(petshop_list)
    else:
        return response.json({"Message": "Nenhum registro de petshop encontrado"})
    

@PETSHOP_ROUTE.route('/get/petshop/<petshop_id:str>/', methods=['GET'])
async def get_one_petshop(request: Request, petshop_id:str):
    try:    
        petshop = collection.find_one({"_id": ObjectId(petshop_id)})
        
        if petshop:
            petshop_instance = PetshopModel(**petshop)
            return response.json(petshop_instance.model_dump())
        else:
            return response.json({"Petshop not found"}, status=404)
        
        
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })
        


@PETSHOP_ROUTE.route('/create/petshop/', methods=['POST', 'GET'])
async def create_petshop(request: Request):
    try:
        petshop = PetshopModel(**request.json)
        
        collection.insert_one(petshop.model_dump())
        
        return response.json({"Message":"Registro adicionado", "Petshop adicionado": petshop.model_dump()})
    
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })
    

@PETSHOP_ROUTE.route('/update/petshop/<petshop_id:str>/', methods=['PUT', 'PATCH', 'GET'])
async def update_petshop(request: Request, petshop_id:str):
    try:
        petshop = collection.find_one({"_id": ObjectId(petshop_id)})
        
        if petshop:
        
            if request.method == "PUT":
                petshop_instance = UpdatePetshopModel(**request.json)
                petshop_dict = petshop_instance.model_dump()
                
                collection.update_one({"_id": ObjectId(petshop_id)}, {"$set": petshop_dict})
            
            if request.method == "PATCH":
                update_petshop_instance = UpdatePetshopModel(**request.json)
                update_petshop_dict = update_petshop_instance.model_dump()
                
                collection.update_one({"_id": ObjectId(petshop_id)}, {"$set": update_petshop_dict})
                
                petshop = collection.find_one({"_id": ObjectId(petshop_id)})
                
                petshop_instance = PetshopModel(**petshop)
                petshop_dict = petshop_instance.model_dump()
        else:
            return response.json({"Petshop not found"}, status=404)
        
        return response.json({"Message": "Petshop atualizado com sucesso", "Petshop atualizado": petshop_dict})
    
    except ValidationError as e:       
        erros = e.errors()
        
        return response.json({"Description": erros[0]["type"],
        "Message error": erros[0]['msg'],
        })
        

@PETSHOP_ROUTE.route('/delete/petshop/<petshop_id:str>/', methods=['DELETE'])
async def delete_one_petshop(request: Request, petshop_id):
    petshop = collection.find_one({"_id": ObjectId(petshop_id)})
    
    if petshop:
        collection.delete_one(petshop)
    
        petshop_dict = PetshopModel(**petshop).model_dump()
        
        return response.json({"Message": "Petshop deletado com sucesso", "Petshop deletado": petshop_dict})
    else:
        return response.json({"Petshop not found"}, status=404)