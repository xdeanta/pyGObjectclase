import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SaludoGlade():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("Formulario.glade")

        senales = {"on_btnSaludo_clicked": self.on_btnSaludo_clicked,
                   "on_txtSaludo_activate": self.on_txtSaludo_activate,
                   "on_winSaludo_delete_event" : Gtk.main_quit}
        builder.connect_signals(senales)

        self.txtSaludo = builder.get_object("txtSaludo")
        self.lblSaludo = builder.get_object("lblSaludo")
        self.winSaludo = builder.get_object("winSaludo")
        self.winSaludo.show_all()

    def on_btnSaludo_clicked(self, boton, datos):

        nombre = self.txtSaludo.get_text()
        self.lblSaludo.set_text("hola, " + nombre + ". Bienvenido")

    def on_txtSaludo_activate(self,boton):

        """
        """

if __name__ == "__main__":
    SaludoGlade()

    Gtk.main()