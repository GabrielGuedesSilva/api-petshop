from typing import List, Optional
from pydantic import BaseModel


class PetshopModel(BaseModel):
    nome_petshop: str
    descricao: str
    

class UpdatePetshopModel(BaseModel):
    nome_petshop: Optional[str] = None
    descricao: Optional[str] = None
    
    def model_dump(self, **kwargs):
        dict_filtrado = super().model_dump(**kwargs)
        return {campo: valor for campo, valor in dict_filtrado.items() if valor is not None}


class PetshopList(BaseModel):
    petshops: List[PetshopModel]
    

class PetModel (BaseModel):
    nome_pet: str
    especie: str
    

class UpdatePetModel(BaseModel):
    nome_pet: Optional[str] = None
    especie: Optional[str] = None
    
    def model_dump(self, **kwargs):
        dict_filtrado = super().model_dump(**kwargs)
        return {campo: valor for campo, valor in dict_filtrado.items() if valor is not None}

    
class PetList(BaseModel):
    pets: List[PetModel]