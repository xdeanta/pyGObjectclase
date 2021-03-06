import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PrimeraVentana():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("PrimeraVentana_glade.glade")

        senal = { "gtk_main_quit" : Gtk.main_quit
                  }

        winPrimeraVentana = builder.get_object("winPrimeraVentana")
        winPrimeraVentana.show_all()

if __name__ == "__main__":
    PrimeraVentana()

    Gtk.main()