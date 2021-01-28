import sqlite3 as dbapi

try:
    bbdd = dbapi.connect ("baseDatosTreeView.dat")
    print (bbdd)


except dbapi.StandardError as e:
    print (e)
else:
    print ("Base de datos aberta")


try:
    cursor = bbdd.cursor ()
    print (cursor)

except dbapi.Error as e:
    print (e)
else:
    print ("Cursor preparado")



try:
    cursor.execute (""" create table usuarios (dni text,
                                               nome text,
                                               direccion text,
                                               edad number,
                                               sexo text)""")

    cursor.execute ("""insert into usuarios
                      values ('3333-A', 'Maria', 'Canceleiro', 24, 'Mujer')""")
    cursor.execute ("""insert into usuarios
                      values ('4444-B', 'Manuel', 'Rosalia', 54, 'Hombre')""")
    cursor.execute ("""insert into usuarios
                      values ('5555-C', 'Ana', 'Areal', 30, 'Mujer')""")
    bbdd.commit()

except dbapi.DatabaseError as e:
    print ("Erro insertando os datos: " + str(e))
else:
    print ("Base de datos creada")
    bbdd.close()