import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

columnas = ["Nombre", "Apellido", "Numero de telefono"]
agendaTel = [["Manuel", "Gil", "986 345 678"],
             ["Ana", "Sáez", "607 891 891"],
             ["Rosa", "Cendón", "678 432 456"],
             ["Raúl", "Pérez", "651 327 453"],
             ["Óscar", "Vila", "986123 321"]]


class EjemploGtkTreeViewTelefonos(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Agenda Telefonica")
        self.set_size_request(200,100)

        mod_agenda = Gtk.ListStore(str,str,str)
        for persona in agendaTel:
            mod_agenda.append(persona)

        tablaAgenda = Gtk.TreeView(model=mod_agenda)

        i = 0
        for columna in columnas:
            celdaRenderer = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(columna, celdaRenderer, text=i)
            col.set_sort_column_id(i)
            tablaAgenda.append_column(col)
            i = i + 1

        tablaAgenda.set_reorderable(True)

        self.add(tablaAgenda)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploGtkTreeViewTelefonos()

    Gtk.main()