import sqlite3 as sql


# En esta seccion tengo que recibir un json y hacer el registo en la base de datos

# Creacion y conexion a la base de datos
createDB = True
dropOldDB = False
if createDB:
    crud.createDb()
dbName = f'dbs/data.sqlite'
conn = sql.connect(dbName)
cur = conn.cursor()

