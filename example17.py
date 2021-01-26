import gi
import sqlite3 as dbapi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class EjemploGtkTreeViewBD(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo 16")
        self.set_size_request(200,100)

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 4)
        modelo = Gtk.ListStore(str,str,str,int, str)
        try:
            bbdd = dbapi.connect("baseDatosTreeView.dat")
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("conexion abierta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("select * from usuarios")
            for fila in cursor.fetchall():
                modelo.append(fila)
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("Consulta ejecutada")
        finally:
            cursor.close()
            bbdd.close()

        vista = Gtk.TreeView(model=modelo)
        vista.set_model(modelo)
        for i, tituloColumna in enumerate(["DNI", "Nombre","Direccion", "Edad", "Sexo"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            vista.append_column(columna)

        cajaV.pack_start(vista,True,True,0)
        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    EjemploGtkTreeViewBD()

    Gtk.main()