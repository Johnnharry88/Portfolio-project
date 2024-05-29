#!/usr/bin/python3
from equi_model.engine.store_json import Store_Json
from equi_model.engine.equi_sql import EquiSQLstore
from os import getenv


#if getenv("EQUIMED_DB_TYPE_STORAGE") == "db":
storage = EquiSQLstore()
#else:
#    storage = Store_Json()

storage.reload()
