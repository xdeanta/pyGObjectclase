import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.overrides.Gio import Gio

class EjemploGtkHeaderBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk.HeaderBar")
        self.set_default_size(200,100)
        self.set_border_width(10)

        cabecera = Gtk.HeaderBar()
        self.set_titlebar(cabecera)
        cabecera.set_show_close_button(True)
        cabecera.props.title = "ejemplo de uso de Gtk.HeaderBar"

        boton = Gtk.Button()
        icono = Gio.ThemedIcon(name = "mail-send-receive-symbolic")
        imagen = Gtk.Image.new_from_gicon (icono,Gtk.IconSize.BUTTON)
        boton.add(imagen)
        boton.connect("clicked", self.on_boton1_clicked)
        cabecera.pack_end(boton)

        caja = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caja.get_style_context(),"linked")

        #boton2 = Gtk.Button()
        self.boton2 = Gtk.Button.new_from_icon_name("pan-end-symbolic", Gtk.IconSize.MENU)
        caja.add(self.boton2)
        cabecera.pack_start(caja)

        self.txvCajaTexto = Gtk.TextView()
        self.add(self.txvCajaTexto)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_boton1_clicked(self,boton):
        buffer = self.txvCajaTexto.get_buffer()
        #buffer.insert_at_cursor("Hola que hace \n")
        buffer.set_text("hola que hace")

if __name__ == "__main__":
    EjemploGtkHeaderBar()

    Gtk.main()