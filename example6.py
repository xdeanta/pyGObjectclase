import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GladePOO(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Saludo usando POO")
        self.set_size_request(200,100)

        caja = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(caja)

        self.lblSaludo = Gtk.Label(label = "Escribe tu nombre")
        caja.pack_start(self.lblSaludo, True, True, 2)

        self.txtSaludo = Gtk.Entry(text = "Escribe aqui tu nombre")
        self.txtSaludo.connect("activate",self.on_btnSaludo_clicked)
        caja.pack_start(self.txtSaludo, True, True, 2)

        self.btnSaludo = Gtk.Button("Saludo")
        self.btnSaludo.connect("clicked",self.on_btnSaludo_clicked)
        caja.pack_start(self.btnSaludo,False,False, 2)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnSaludo_clicked(self, boton):

        nombre = self.txtSaludo.get_text()
        self.lblSaludo.set_text("hola, " + nombre + ". Bienvenido")


if __name__ == "__main__":
    GladePOO()

    Gtk.main()