from sanic import Blueprint
from .petshop_route import PETSHOP_ROUTE
from .pet_route import PET_ROUTE

ROUTES = Blueprint.group(
    PETSHOP_ROUTE,
    PET_ROUTE
)