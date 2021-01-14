import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class EjemploGtkTreeViewTelefonos(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo 15")
        self.set_size_request(200,100)

        modelo = Gtk.TreeStore(str, int)

        for avo in range(5):
            idavo = modelo.append(None,["Avó" + str(avo),avo])
            for pai in range(4):
                idPai= modelo.append(idavo, ["Pai % i do avó % i" % (pai,avo),pai])
                for fillo in range(3):
                    modelo.append(idPai, ["Fillo %i do pai %i, do avó %i" % (fillo,pai,avo), fillo])

        vista = Gtk.TreeView(modelo)
        tvColumna = Gtk.TreeViewColumn("Parentesco")
        celda = Gtk.CellRendererText()
        tvColumna.pack_start(celda, True)
        tvColumna.add_attribute(celda, "text", 0)
        vista.append_column(tvColumna)

        tvColumna2 = Gtk.TreeViewColumn("Orde")
        celda2 = Gtk.CellRendererText()
        tvColumna2.pack_start(celda2, True)
        tvColumna2.add_attribute(celda2, "text", 1)
        vista.append_column(tvColumna2)

        self.add(vista)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploGtkTreeViewTelefonos()

    Gtk.main()