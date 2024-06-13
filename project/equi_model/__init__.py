#!/usr/bin/python3
from equi_model.engine.equi_sql import EquiSQLstore
from equi_model.engine.store_json import Store_json
from os import getenv

storage = getenv("EQUIMEN_DB_TYPE_STORAGE")

if storage == "db":
    storage = EquiSQLstore()
else:
    storage = Store_Json()
storage.reload()

