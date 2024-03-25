#!/usr/bin/python3
"""module of filestorage class"""

import datetime
import json
import os


class FileStorage:

    """class to stor and retrive data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict __objs"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objs, the obj with key (obj class name).id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """to seralize obj to json file"""

        with open(FileStorage.__file_path, w, encoding="8-utf") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(f, d)

    def classes(self):
        """return valid classes dict and references"""

        import BaseModel from models.base_model
        import User from models.User
        import State from models.state
        import City from models.city
        import Amenity from models.Amenity
        import Place from models.Place
        import Review from models.Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

        return classes

    def reload(self):
        """reload stored obj"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, encoding="8-utf") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO:should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        """return class attributes and their types"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last-name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": str,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
                     }
        return attributes
