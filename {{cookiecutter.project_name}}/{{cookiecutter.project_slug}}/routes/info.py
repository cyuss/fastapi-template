# -*- coding: utf-8 -*-

from typing import Dict, Union

from fastapi import APIRouter, Depends
from loguru import logger

from ..core import settings
from .schemas import InfoOut


router = APIRouter()


@router.get("/info", response_model=InfoOut)
def info(
        settings: settings.Settings = Depends(settings.get_settings)
) -> Dict[str, Union[str, None]]:
    """Return the API metadata to the user.

    Parameters
    ----------
    settings : settings.Settings
        Metadata defined in the app settings.
    """
    logger.info("API Metadata requested.")

    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_description": settings.app_description,
        "author": settings.author,
        "host": settings.host,
        "port": settings.port
    }
