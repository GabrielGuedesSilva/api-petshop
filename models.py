from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, RootModel, field_serializer


class PetModel (BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    nome_pet: str
    especie: str

    model_config = ConfigDict(
        arbitrary_types_allowed=True)

    @field_serializer('id')
    def serialize_id(self, id):
        return str(id)


class UpdatePetModel(BaseModel):
    nome_pet: Optional[str] = None
    especie: Optional[str] = None


class PetList(RootModel):
    root: List[PetModel]


class PetshopModel(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    nome_petshop: str
    descricao: str

    model_config = ConfigDict(
        arbitrary_types_allowed=True)

    @field_serializer('id')
    def serialize_id(self, id):
        return str(id)


class UpdatePetshopModel(BaseModel):
    nome_petshop: Optional[str] = None
    descricao: Optional[str] = None


class PetshopList(RootModel):
    root: List[PetshopModel]
