import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GladePOO(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Saludo usando POO")
        self.set_size_request(200,100)

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(cajaV)


        self.lblSaludo = Gtk.Label(label = "Escribe tu nombre")
        cajaV.pack_start(self.lblSaludo, True, True, 2)

        self.txtSaludo = Gtk.Entry(text = "Escribe aqui tu nombre")
        self.txtSaludo.connect("activate",self.on_btnSaludo_clicked,"Saludo")
        cajaV.pack_start(self.txtSaludo, True, False, 2)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        cajaV.pack_start(cajaH,True, True, 2)

        self.btnSaludo = Gtk.Button(label="Saludo")
        self.btnSaludo.connect("clicked",self.on_btnSaludo_clicked, "Saludo")
        cajaV.pack_start(self.btnSaludo,True,False, 2)

        self.btnDespedida = Gtk.Button(label="Despedida")
        self.btnDespedida.connect("clicked", self.on_btnSaludo_clicked, "Despedida")
        cajaH.pack_start(self.btnDespedida, True, False, 2)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnSaludo_clicked(self, boton,tipo):

        nombre = self.txtSaludo.get_text()
        if nombre != "":
            if nombre == "Saludo":
                self.lblSaludo.set_text("hola, " + nombre + ". Bienvenido")
                self.txtSaludo.set_text("")
            if nombre == "Despedida":
                self.lblSaludo.set_text("Hasta luego, " + nombre + ".")
                self.txtSaludo.set_text("")


if __name__ == "__main__":
    GladePOO()

    Gtk.main()