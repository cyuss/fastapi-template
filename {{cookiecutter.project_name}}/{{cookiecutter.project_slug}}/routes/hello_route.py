# -*- coding: utf-8 -*-

from fastapi import APIRouter
from loguru import logger
from starlette.requests import Request


router = APIRouter()

@router.post("/hello")
async def predict():
    return {'results': "Congrats !"}
