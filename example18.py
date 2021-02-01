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
                print(fila)
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

        seleccion = vista.get_selection()
        seleccion.connect("changed", self.on_vista_selection_changed)
        for i, tituloColumna in enumerate(["DNI", "Nombre","Direccion", "Edad", "Sexo"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            celda.props.editable= True
            #celda.connect("edited", self.on_celda_edited, i, modelo)
            vista.append_column(columna)

        """celda = Gtk.CellRendererCombo()
        modeloCellRendererCombo = celda.get_model()
        modeloCellRendererCombo.append("Hombre")
        modeloCellRendererCombo.append("Mujer")
        columna = Gtk.TreeViewColumn("Sexo", celda, text=4)
        celda.connect("changed", self.on_celda_changed, modelo, 4)"""

        cajaV.pack_start(vista,True,True,0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.chkHome = Gtk.CheckButton(label="Home")
        self.chkHome.connect("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        self.chkMuller = Gtk.CheckButton(label="Muller")
        self.chkMuller.connect("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        caixaH.pack_start(self.chkHome, False, False, 2)
        caixaH.pack_start(self.chkMuller, False, False, 2)
        cajaV.pack_start(caixaH, True, True, 0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.txtDni = Gtk.Entry()
        self.txtNombre = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtEdad = Gtk.Entry()
        self.cmbSexo = Gtk.ComboBoxText()
        self.cmbSexo.append_text("Hombre")
        self.cmbSexo.append_text("Mujer")
        caixaH.pack_start(self.txtDni, True, False, 2)
        caixaH.pack_start(self.txtNombre, True, False, 2)
        caixaH.pack_start(self.txtDireccion, True, False, 2)
        caixaH.pack_start(self.txtEdad, True, False, 2)
        caixaH.pack_start(self.cmbSexo, True, False, 2)
        cajaV.pack_start(caixaH, True, False, 2)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.btnModificar = Gtk.Button(label = "Modificar")
        self.btnAnadir = Gtk.Button(label="Añadir")
        self.btnModificar.connect("clicked" , self.on_btnModificar_clicked, seleccion)
        self.btnAnadir.connect("clicked", self.on_btnAnadir_clicked, modelo)
        caixaH.pack_start(self.btnModificar, False, False, 2)
        caixaH.pack_start(self.btnAnadir, False, False, 2)
        cajaV.pack_start(caixaH, True, False, 2)


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

    def on_celda_changed(self, combo, columna, fila, elemento, modelo):
        modelo [fila][columna] = combo.get_model()[elemento]

    def on_vista_selection_changed(self, selection):
        modelo , fila = selection.get_selected()
        if fila is not None:
            self.txtDni.set_text(modelo[fila][0])
            self.txtNombre.set_text(modelo[fila][1])
            self.txtDireccion.set_text(modelo[fila][2])
            self.txtEdad.set_text(str(modelo[fila][3]))
            for i,elemento in enumerate(self.cmbSexo.get_model()):
                if elemento[0] == modelo [fila][4]:
                    self.cmbSexo.set_active(i)

    def on_btnModificar_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo[fila][0] = self.txtDni.get_text()
            modelo[fila][1] = self.txtNombre.get_text()
            modelo[fila][2] = self.txtDireccion.get_text()
            modelo[fila][3] = int(self.txtEdad.get_text())
            modelo[fila][4] = self.cmbSexo.get_active_text()

        try:
            bbdd = dbapi.connect("baseDatosTreeView.dat")
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("conexion abierta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("UPDATE usuarios SET nome = ?, direccion = ?, edad = ?, sexo =? WHERE dni = ?", ())
            for fila in cursor.fetchall():
                modelo.append(fila)
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("Consulta ejecutada")
        finally:
            cursor.close()
            bbdd.close()

    def on_btnAnadir_clicked(self, boton, modelo):
        entry = [self.txtDni.get_text(), self.txtNombre.get_text(), self.txtDireccion.get_text(), int(self.txtEdad.get_text()), self.cmbSexo.get_active_text()]
        modelo.append(entry)
        try:
            bbdd = dbapi.connect("baseDatosTreeView.dat");
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("conexion abierta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("INSERT INTO usuarios values (?,?,?,?,?)", entry)
            bbdd.commit()
        except dbapi.DatabaseError as e:
            print(e)
        else:
            print("dato insertado")
        finally:
            cursor.close()
            bbdd.close()
        """Algo"""

if __name__ == "__main__":
    EjemploGtkTreeViewBD()

    Gtk.main()