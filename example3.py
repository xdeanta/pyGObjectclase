import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PrimeraVentana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Primera Ventana")
        self.set_default_size( 300,200)

        btnSalida = Gtk.Button()
        btnSalida.set_label("Salir")
        btnSalida.connect("clicked", self.on_btnSalida_clicked, "Los datos que considere oportuno")
        self. add(btnSalida)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnSalida_clicked(self,control, datos):
        print(datos)
        Gtk.main_quit()

if __name__ == "__main__":
    PrimeraVentana()

    Gtk.main()