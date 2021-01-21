import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class EjemploGtkTreeViewToggle(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo 16")
        self.set_size_request(200,100)

        modelo = Gtk.ListStore(str, bool)
        modelo.append(["Ethernet", True])
        modelo.append(["Wireless", True])
        modelo.append(["Bluetooth", False])
        modelo.append(["Movil 3G", True])

        vista = Gtk.TreeView(model = modelo)

        cellRenderderText = Gtk.CellRendererText()
        #permite editar el modelo y detectar cuando se edita
        cellRenderderText.props.editable = True
        cellRenderderText.connect("edited", self.on_celdaTexto_edited, modelo)

        trcColumna = Gtk.TreeViewColumn("Tipo Conexion")
        trcColumna.pack_start(cellRenderderText,False)
        trcColumna.add_attribute(cellRenderderText,"text", 0)
        vista.append_column(trcColumna)

        cellRenderderToggle = Gtk.CellRendererToggle()
        cellRenderderToggle.connect("toggled" , self.on_celda_toggled, modelo)

        trcColumna = Gtk.TreeViewColumn("Estado")
        trcColumna.pack_start(cellRenderderToggle, False)
        trcColumna.add_attribute(cellRenderderToggle, "active", 1)
        vista.append_column(trcColumna)

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        cajaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        lblTipo = Gtk.Label(label = "Tipo")
        txtTipo = Gtk.Entry()

        chkEstado = Gtk.CheckButton()
        chkEstado.set_label(("Estado"))
        cajaH.pack_start(lblTipo, False, False, 0)
        cajaH.pack_start(txtTipo, True, False, 0)
        cajaH.pack_start(chkEstado, False, False, 0)
        cajaV.pack_start(cajaH, True, True, 0)

        cajaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        btnAceptar = Gtk.Button(label = "Aceptar")
        btnCancelar = Gtk.Button(label = "Cancelar")
        cajaH2.pack_end(btnCancelar, True, True, 0)
        cajaH2.pack_end(btnAceptar, True, True, 0)
        cajaV.pack_start(cajaH2, True, True, 0)

        self.add(vista)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_celda_toggled(self, celda, fila, modelo):
        modelo[fila][1] = not modelo [fila] [1] #asi activa y deactiva el checkbox
        print("usuario hizo click")

    def on_celdaTexto_edited(self,celda, fila, texto, modelo): #recibe el texto de la edicion y modifica el modelo
        modelo [fila][0] = texto

if __name__ == "__main__":
    EjemploGtkTreeViewToggle()

    Gtk.main()