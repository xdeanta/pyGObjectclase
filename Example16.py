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
        #trcColumna.pack_start(cellRenderderText, False)
        #trcColumna.add_attribute(cellRenderderText, "text", 1)
        trcColumna.add_attribute(cellRenderderToggle, "active", 1)
        vista.append_column(trcColumna)

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