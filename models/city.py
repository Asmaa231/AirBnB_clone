#!/usr/bin/python3
"""user class module"""

import BaseModel from models.base_model


class City(BaseModel):
    """manage city objects class"""

    state_id = ""
    name = ""
