from fastapi import APIRouter

from {{cookiecutter.project_slug}}.routes import hello_route


api_router = APIRouter()

api_router.include_router(hello_route.router, tags=['data_augmentation'])
