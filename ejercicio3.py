import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class EjerIU(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejercicio 3")
        self.set_size_request(500,400)
        self.set_border_width(10)

        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(box)

        etiqueta = Gtk.Label(label = "Informacion del producto")
        cuadro1 = Gtk.Frame(label = "Datos Basicos")
        cuadro2 = Gtk.Frame(label = "Datos Economicos")
        box.pack_start(etiqueta, False, False, 1)
        box.pack_start(cuadro1, True, True, 20)
        box.pack_start(cuadro2, True, True, 20)

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        cuadro1.add(cajaV)
        lblnombre = Gtk.Label(label = "Nombre")
        txtNombre = Gtk.Entry()
        lblDesc = Gtk.Label(label = "Descripcion")
        txtvDesc = Gtk.TextView()

        cajaH = Gtk.Box(spacing = 2)
        chkContador = Gtk.CheckButton(label = "Añadir contador de visitas")
        cajaV.pack_start(lblnombre, False, False, 2)
        cajaV.pack_start(txtNombre, True, False, 2)
        cajaV.pack_start(lblDesc, False, False, 2)
        cajaV.pack_start(txtvDesc, True, True, 2)
        cajaV.pack_start(cajaH, True, True, 2)
        cajaV.pack_start(chkContador, False, False, 2)

        lblFoto = Gtk.Label(label = "Foto")
        txtFoto = Gtk.Entry()
        btnElegirFoto = Gtk.Button(label = "Elegir...")
        cajaH.pack_start(lblFoto, False, False, 2)
        cajaH.pack_start(txtFoto, False, False, 2)
        cajaH.pack_start(btnElegirFoto, False, False, 2)

        caja2V = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        cuadro2.add(caja2V)
        caja2H = Gtk.Box(spacing = 6)
        lblPromo = Gtk.Label(label = "Promocion")
        rbtnNinguno = Gtk.RadioButton(label ="Ninguno")
        rbtnTrans = Gtk.RadioButton(label = "Transporte Gratuito")
        rbtnDescuento = Gtk.RadioButton(label = "Descuento 5%")
        caja2V.pack_start(caja2H, False, False, 2)
        caja2V.pack_start(lblPromo, False, False, 2)
        caja2V.pack_start(rbtnNinguno, False, False, 2)
        caja2V.pack_start(rbtnTrans, False, False, 2)
        caja2V.pack_start(rbtnDescuento, False, False, 2)

        lblPrecio = Gtk.Label(label = "Precio")
        txtPrecio = Gtk.Entry()
        lblSimbolo = Gtk.Label(label = "€")
        lblImpuesto = Gtk.Label(label = "Impuestos")
        cmbImpuesto = Gtk.ComboBoxText()
        cmbImpuesto.append_text("4%")
        cmbImpuesto.append_text("7%")
        cmbImpuesto.append_text("14%")
        cmbImpuesto.append_text("25%")
        caja2H.pack_start(lblPrecio, False, False, 2)
        caja2H.pack_start(txtPrecio, False, False, 2)
        caja2H.pack_start(lblSimbolo, False, False, 2)
        caja2H.pack_start(lblImpuesto, False, False, 2)
        caja2H.pack_start(cmbImpuesto, False, False, 2)


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    EjerIU()

    Gtk.main()