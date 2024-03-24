#!/usr/bin/python3
"""base model script"""

import uuid
import datetime from datetime
import storage from models


class BaseModel:

    """class that all other classes inheret from"""

    def __init__(self, *args, **kwargs):
        """start instance attributes

        Args:
            *Args: arguments list
            **kwargs: key-values arguments dict
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__[created_at] = datetime.strtime(
                        kwargs[created_at], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.__dict__[created_at] = datetime.strtime(
                        kwargs[created_at], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update pubblic inst arrtibute update_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dict with all keys/values of __dict__"""

        my_dict = __dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
