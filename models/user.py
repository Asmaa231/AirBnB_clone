#!/usr/bin/python3
"""user class module"""

import BaseModel from models.base_model


class User(BaseModel):
    """manage user objects class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
