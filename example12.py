import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk

class FilaListBoxConDatos(Gtk.ListBoxRow):
    def __init__(self,dato):
        super(Gtk.ListBoxRow,self).__init__()
        self.add(Gtk.Label(label = dato))

class EjemploGtkHeaderBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk.HeaderBar")
        self.set_border_width(10)

        cajaExterna = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(cajaExterna)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        cajaExterna.pack_start(listbox, True, True,0)

        row = Gtk.ListBoxRow()
        cajaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(cajaH)
        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        cajaH.pack_start(cajaV, True, True,0)

        etiqueta1 = Gtk.Label(label = "Fecha y Hora Automatica", xalign=0)
        etiqueta2 = Gtk.Label(label="Requiere Acceso a Internet", xalign=0)
        cajaV.pack_start(etiqueta1, True, True, 0)
        cajaV.pack_start(etiqueta2, True, True, 0)

        interruptor = Gtk.Switch()
        interruptor.props.valign = Gtk.Align.CENTER
        cajaH.pack_start(interruptor, False, True, 0)

        listbox.add(row)

        fila = Gtk.ListBoxRow()
        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        fila.add(cajaH)
        etiqueta3 = Gtk.Label(label="Formato de fecha", xalign=0)

        combo = Gtk.ComboBoxText()
        combo.insert(0 , "0", "24-Horas")
        combo.insert(1, "1", "AM/PM")
        cajaH.pack_start(etiqueta3, True, True, 0)
        cajaH.pack_start(combo, False, True, 0)

        listbox.add(fila)

        listbox2 = Gtk.Box()
        elementos = "Esto es un ListBox mal ordenado".split()

        for elemento in elementos:
            listbox2.add(FilaListBoxConDatos(elemento))

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploGtkHeaderBar()

    Gtk.main()