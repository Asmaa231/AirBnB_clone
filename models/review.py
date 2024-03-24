#!/usr/bin/python3
"""review class module"""

import BaseModel from models.base_model


class Review(BaseModel):
    """manage review objects class"""

    place_id = ""
    user_id = ""
    text = ""
