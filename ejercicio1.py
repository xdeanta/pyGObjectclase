import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GladePOO(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejercicio 1")
        self.set_size_request(200,100)

        grid=Gtk.Grid()
        self.add(grid)

        self.lblSaludo = Gtk.Label(label = "Escribe tu nombre")
        self.txtSaludo = Gtk.Entry(text="Escribe tu nombre aqui")
        self.btnSaludo = Gtk.Button(label="Saludar")
        self.btnDespedida = Gtk.Button(label="Despedir")

        grid.attach(self.lblSaludo, 0, 0, 2, 1)
        grid.attach(self.txtSaludo, 0, 1, 2, 1)
        grid.attach(self.btnSaludo, 0, 2, 1, 1)
        grid.attach(self.btnDespedida, 1, 2, 1, 1)

        self.connect("delete-event", Gtk.main_quit)
        self.btnSaludo.connect("clicked", self.on_btnSaludo_clicked, "Saludo")
        self.btnDespedida.connect("clicked", self.on_btnSaludo_clicked, "Despedida")
        self.show_all()

    def on_btnSaludo_clicked(self, boton, tipo):
        nombre = self.txtSaludo.get_text()
        if nombre != "":
            if tipo == "Saludo":
                self.lblSaludo.set_text("hola, " + nombre + ". Bienvenido")
                self.txtSaludo.set_text("")
            if tipo == "Despedida":
                self.lblSaludo.set_text("Hasta luego, " + nombre + ".")
                self.txtSaludo.set_text("")


if __name__ == "__main__":
    GladePOO()

    Gtk.main()