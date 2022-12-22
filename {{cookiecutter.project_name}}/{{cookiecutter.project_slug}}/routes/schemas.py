# -*- coding: utf-8 -*-

from typing import Dict, List, Optional

from enum import Enum
from pydantic import BaseModel, Field


# --------------------- EXAMPLES ---------------------


# ---------------------- INPUTS ----------------------
class InfoIn(BaseModel):
    pass

# ---------------------- OUTPUTS ----------------------
class InfoOut(BaseModel):
    app_name: str
    app_version: str
    app_description: str
    author: Optional[str] = None
    host: str
    port: str
