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

        self.filtrado_sexo = "None"
        filtro_usuarios = modelo.filter_new()
        filtro_usuarios.set_visible_func(self.filtro_usuarios_sexo)


        vista = Gtk.TreeView(model=filtro_usuarios)
        for i, tituloColumna in enumerate(["DNI", "Nombre","Direccion", "Edad", "Sexo"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            vista.append_column(columna)

        cajaV.pack_start(vista,True,True,0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.chkHome = Gtk.CheckButton(label="Home")
        self.chkHome.connect("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        self.chkMuller = Gtk.CheckButton(label="Muller")
        self.chkMuller.connect("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        caixaH.pack_start(self.chkHome, False, False, 2)
        caixaH.pack_start(self.chkMuller, False, False, 2)
        cajaV.pack_start(caixaH, True, True, 0)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def filtro_usuarios_sexo(self, modelo, fila, datos):
        if (self.filtrado_sexo is None or self.filtrado_sexo == "None"):
            return True
        else:
            return modelo[fila][4] == self.filtrado_sexo

    def on_chkXenero_toggled(self, control, modelo):
        if self.chkMuller.get_active() and self.chkHome.get_active() == False:
            self.filtrado_sexo = "Mujer"
        elif self.chkMuller.get_active() == False and self.chkHome.get_active():
                self.filtrado_sexo = "Hombre"
        else:
            self.filtrado_sexo = "None"
        modelo.refilter()

if __name__ == "__main__":
    EjemploGtkTreeViewBD()

    Gtk.main()