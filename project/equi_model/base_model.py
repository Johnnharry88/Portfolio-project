#!/usr/bin/python3
"""Module that holds a general attribute for other class
"""
import equi_model 
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


Base = declarative_base()


class BaseModel:
    """Class that defines common attributes
    and method for class inheritance
    """
    if getenv("EQUIMED_DB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
        updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *arg, **kwarg):
        """Constructor that instiantiates object
        using its attributes
        """
        if len(kwarg) > 0:
            for k, v in kwarg.items():
                if k == '__class__':
                    continue
                if k == 'created_at':
                    v = datetime.fromisoformat(v)
                if k == 'updated_at':
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        equi_model.storage.new(self)

    def __str__(self):
        """String Representation of instance
        """
        return "[{}] ({}) {}". format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates changes using the current date and time
        and saves it to Json file"""
        self.updated_at = datetime.now()
        equi_model.storage.save()
  
    def dict_pro(self):
        """return a dictionary containing all 
        keys/values of __dict__ of instance
        """
        dict_x = dict(self.__dict__)
        dict_x['__class__'] = str(type(self).__name__)
        dict_x['created_at'] = self.created_at.isoformat()
        dict_x['updated_at'] = self.updated_at.isoformat()
        return dict_x
