#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
#from equi_model.__init__ import storage
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from equi_model.order import Order


class User(BaseModel, Base):
    """Represents a User """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=True)
    address = Column(String(128), nullable=False)
    phone_no = Column(Integer, nullable=False)
    orders = relationship("Order", cascade='all, delete, delete-orphan',
                            backref="user")
#    else:
#        first_name = ''
#        last_name = ''
#        email = ''
#        password = ''
#        address = ''
#        phone_no = ''
