import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Template(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Template")
        self.set_size_request(200, 100)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Template()

    Gtk.main()