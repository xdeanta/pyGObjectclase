import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculadora(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")
        self.set_size_request(500,400)

        grid = Gtk.Grid()
        self.add(grid)
        boton1 = Gtk.Button(label="1")
        boton2 = Gtk.Button(label="2")
        boton3 = Gtk.Button(label="3")
        boton4 = Gtk.Button(label="4")
        boton5 = Gtk.Button(label="5")
        boton6 = Gtk.Button(label="6")
        boton7 = Gtk.Button(label="7")
        boton8 = Gtk.Button(label="8")
        boton9 = Gtk.Button(label="9")
        boton0 = Gtk.Button(label="0")
        botonIgual = Gtk.Button(label="=")
        botonSuma = Gtk.Button(label="+")
        botonResta = Gtk.Button(label="-")
        botonMulti = Gtk.Button(label="*")
        botonDiv = Gtk.Button(label="/")

        grid.add(boton1)
        grid.attach(boton2, 1,0, 2, 1)
        grid.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(boton5, 1, 2, 1, 1)
        grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Calculadora()

    Gtk.main()