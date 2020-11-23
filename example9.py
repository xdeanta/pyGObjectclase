import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class EjemploGtkStack(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk.Stack y Gtk.StackSwitcher")
        self.set_size_request(200,100)

        cajaV=Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=6)
        self.add(cajaV)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        botonCheck = Gtk.CheckButton (label="Presioname")
        stack.add_titled(botonCheck, "Chequeo" , "Boton de chequeo")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        etiqueta = Gtk.Label()
        etiqueta.set_markup("<big>Etiqueta elegante</big>")
        stack.add_titled(etiqueta, "Etiqueta", "Una etiqueta")
        stack_switcher.set_stack(stack)

        cajaV.pack_start(stack_switcher, True, True, 0)
        cajaV.pack_start(stack,True,True,0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

class Panel(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)

        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")

        self.add(boton1)
        self.attach(boton2, 1, 0, 2, 1)
        self.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        self.attach(boton5, 1, 2, 1, 1)
        self.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

class EjemploGtkNoteBook(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk.Stack y Gtk.StackSwitcher")
        self.set_size_request(200, 100)

        self.notebook = Gtk.Notebook(self)


if __name__ == "__main__":
    EjemploGtkStack()

    Gtk.main()