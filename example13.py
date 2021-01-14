import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class EjemploComboBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Saludo usando POO")
        self.set_size_request(200,100)

        lstNombres = Gtk.ListStore(int, str)
        lstNombres.append([16, "Juan"])
        lstNombres.append([11, "Pedro"])
        lstNombres.append([6, "Ana"])
        lstNombres.append([13, "Rosa"])
        lstNombres.append([19, "Jose"])

        cajaV=Gtk.Box (orientation = Gtk.Orientation.VERTICAL)

        cmbNombres = Gtk.ComboBox.new_with_model_and_entry(lstNombres)
        cmbNombres.connect("changed", self.on_cmbNombres_changed)
        cmbNombres.set_entry_text_column(1)
        cajaV.pack_start(cmbNombres, False, False,0)

        txtNombre = cmbNombres.get_child()
        txtNombre.connect("activate", self.on_txtNombres_activated, lstNombres, cmbNombres)

        modelo_frutas = Gtk.ListStore(str)
        frutas= ["Manzana", "Pera", "Uva", "Melon", "Piña"]

        for fruta in frutas:
            modelo_frutas.append([fruta])

        cmbFrutas = Gtk.ComboBox.new_with_model(modelo_frutas)
        cmbFrutas.connect("changed", self.on_cmbFrutas_changed)
        renderer_text = Gtk.CellRendererText()
        cmbFrutas.pack_start(renderer_text,True)
        cmbFrutas.add_attribute(renderer_text,"text", 0)
        cajaV.pack_start(cmbFrutas, False, False, 0)

        self.add(cajaV)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cmbNombres_changed(self, combo):
        fila=combo.get_active_iter()
        if fila is not None:
            modelo=combo.get_model()
            edad, nombre = modelo[fila][:2]
            print("Seleccionado: edad=%d, nombre=%s" % (edad,nombre))
        else:
            txtNombre= combo.get_child()
            print("Escrito: %s" % txtNombre.get_text())

    def on_txtNombres_activated(self, control, listaNombres):
        nombre= control.get_text()
        listaNombres.append([99,nombre])
        control.set_text("")

    def on_cmbFrutas_changed(self, combo):
        fila=combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            fruta = modelo[fila][0]
            print("La fruta elegida es: %s" % fruta)

if __name__ == "__main__":
    EjemploComboBox()

    Gtk.main()