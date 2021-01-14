import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

columnas = ["Nombre", "Apellido", "Numero de telefono"]
agendaTel= ["Manuel" , "Gil", "986 231 543"]

class EjemploGtkTreeViewTelefonos(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Saludo usando POO")
        self.set_size_request(200,100)

        mod_agenda = Gtk.ListStore(str,str,str)
        for persona in agendaTel:
            mod_agenda.append([persona])
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploGtkTreeViewTelefonos()

    Gtk.main()