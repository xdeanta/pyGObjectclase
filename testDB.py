import sqlite3 as dbapi

#print (dbapi.apilevel)
#print (dbapi.threadsafety)
#print (dbapi.paramstyle)

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
    cursor.execute ("select * from usuarios")

    #fetchone a seguinte tupla
    #fetchall devolta un obxecto iterable con todalas tuplas
    #fetcmany numero de tuplas pasado por parametro

    for fila in cursor.fetchall():
        #print (fila)
        print ( "Nome: "+ fila [1])
        print ( "DNI: " + fila [0])
        print ( "Direccion: " + fila[2])

except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: " + str(e))
else:
    print("Consulta executada")

finally:
    cursor.close()
    bbdd.close()