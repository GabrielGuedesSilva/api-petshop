from typing import List, Optional
from pydantic import BaseModel, RootModel, Field, ConfigDict
from utils import PyObjectId



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


class PetModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nome_pet: str
    especie: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True)
    

class UpdatePetModel(BaseModel):
    nome_pet: Optional[str] = None
    especie: Optional[str] = None
    
    def model_dump(self, **kwargs):
        dict_filtrado = super().model_dump(**kwargs)
        return {campo: valor for campo, valor in dict_filtrado.items() if valor is not None}

    
class PetList(RootModel):
    root: List[PetModel]