from fastapi import APIRouter

from {{cookiecutter.project_slug}}.routes import info


api_router = APIRouter()

api_router.include_router(info.router, tags=["metadata"])
