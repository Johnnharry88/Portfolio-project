#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Date, ForeignKey


class Order(BaseModel, Base):
    if getenv("EQUIMED_DB_TYPE_STORAGE") == "db":
        __tablename__ = "orders"
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        date = Column(Date, default = datetime.date.today(), nullable=False)
