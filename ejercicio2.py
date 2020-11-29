import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculadora(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")
        self.set_size_request(200,150)
        #Grid
        grid = Gtk.Grid()
        self.add(grid)

        #botones

        self.boton1 = Gtk.Button(label="1")
        self.boton2 = Gtk.Button(label="2")
        self.boton3 = Gtk.Button(label="3")
        self.boton4 = Gtk.Button(label="4")
        self.boton5 = Gtk.Button(label="5")
        self.boton6 = Gtk.Button(label="6")
        self.boton7 = Gtk.Button(label="7")
        self.boton8 = Gtk.Button(label="8")
        self.boton9 = Gtk.Button(label="9")
        self.boton0 = Gtk.Button(label="0")
        self.botonIgual = Gtk.Button(label="=")
        self.botonSuma = Gtk.Button(label="+")
        self.botonResta = Gtk.Button(label="-")
        self.botonMulti = Gtk.Button(label="*")
        self.botonDiv = Gtk.Button(label="/")
        self.botonDec = Gtk.Button(label=".")

        #Pantalla

        self.Screen = Gtk.Entry()

        #Conexiones

        self.boton1.connect("clicked",self.on_boton1_clicked)
        self.boton2.connect("clicked", self.on_boton2_clicked)
        self.boton3.connect("clicked", self.on_boton3_clicked)
        self.boton4.connect("clicked", self.on_boton4_clicked)
        self.boton5.connect("clicked", self.on_boton5_clicked)
        self.boton6.connect("clicked", self.on_boton6_clicked)
        self.boton7.connect("clicked", self.on_boton7_clicked)
        self.boton8.connect("clicked", self.on_boton8_clicked)
        self.boton9.connect("clicked", self.on_boton9_clicked)
        self.boton0.connect("clicked", self.on_boton0_clicked)
        self.botonDec.connect("clicked", self.on_botonDec_clicked)

        self.botonSuma.connect("clicked", self.on_botonSuma_clicked)
        self.botonResta.connect("clicked", self.on_botonResta_clicked)
        self.botonMulti.connect("clicked", self.on_botonMulti_clicked)
        self.botonDiv.connect("clicked", self.on_botonDiv_clicked)
        self.botonIgual.connect("clicked", self.on_botonIgual_clicked)

        #Configuracion de la ventana

        grid.attach(self.Screen, 0, 0, 4, 1)
        grid.attach(self.boton1, 0, 1, 1, 1)
        grid.attach(self.boton2, 1, 1, 1, 1)
        grid.attach(self.boton3, 2, 1, 1, 1)
        grid.attach(self.boton4, 0, 2, 1, 1)
        grid.attach(self.boton5, 1, 2, 1, 1)
        grid.attach(self.boton6, 2, 2, 1, 1)
        grid.attach(self.boton7, 0, 3, 1, 1)
        grid.attach(self.boton8, 1, 3, 1, 1)
        grid.attach(self.boton9, 2, 3, 1, 1)
        grid.attach(self.boton0, 1, 4, 1, 1)
        grid.attach(self.botonDec, 0, 4, 1, 1)
        grid.attach(self.botonIgual, 2, 4, 1, 1)
        grid.attach(self.botonSuma, 3, 1, 1, 1)
        grid.attach(self.botonResta, 3, 2, 1, 1)
        grid.attach(self.botonMulti, 3, 3, 1, 1)
        grid.attach(self.botonDiv, 3, 4, 1, 1)


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_boton1_clicked(self,boton):
        numero = self.Screen.get_text() + "1"
        self.Screen.set_text(numero)

    def on_boton2_clicked(self,boton):
        numero = self.Screen.get_text() + "2"
        self.Screen.set_text(numero)

    def on_boton3_clicked(self,boton):
        numero = self.Screen.get_text() + "3"
        self.Screen.set_text(numero)

    def on_boton4_clicked(self, boton):
        numero = self.Screen.get_text() + "4"
        self.Screen.set_text(numero)

    def on_boton5_clicked(self, boton):
        numero = self.Screen.get_text() + "5"
        self.Screen.set_text(numero)

    def on_boton6_clicked(self, boton):
        numero = self.Screen.get_text() + "6"
        self.Screen.set_text(numero)

    def on_boton7_clicked(self, boton):
        numero = self.Screen.get_text() + "7"
        self.Screen.set_text(numero)

    def on_boton8_clicked(self, boton):
        numero = self.Screen.get_text() + "8"
        self.Screen.set_text(numero)

    def on_boton9_clicked(self, boton):
        numero = self.Screen.get_text() + "9"
        self.Screen.set_text(numero)

    def on_boton0_clicked(self, boton):
        numero = self.Screen.get_text() + "0"
        self.Screen.set_text(numero)

    def on_botonSuma_clicked(self, boton):
        numero = self.Screen.get_text() + "+"
        self.Screen.set_text(numero)

    def on_botonResta_clicked(self, boton):
        numero = self.Screen.get_text() + "-"
        self.Screen.set_text(numero)

    def on_botonMulti_clicked(self, boton):
        numero = self.Screen.get_text() + "*"
        self.Screen.set_text(numero)

    def on_botonDiv_clicked(self, boton):
        numero = self.Screen.get_text() + "/"
        self.Screen.set_text(numero)

    def on_botonDec_clicked(self, boton):
        numero = self.Screen.get_text() + "."
        self.Screen.set_text(numero)

    def on_botonIgual_clicked(self, boton):
        Ops = self.Screen.get_text()
        print(Ops)
        print(Ops.find("+"))
        if Ops.find("+") > 0:
            operandos = Ops.split("+")
            op1=float(operandos[0])
            print(op1)
            op2=float(operandos[1])
            ret=op1+op2
            #print(ret)
            self.Screen.set_text(str(ret))
        elif Ops.find("-") > 0:
            operandos = Ops.split("-")
            op1 = float(operandos[0])
            op2 = float(operandos[1])
            ret = op1 - op2
            # print(ret)
            self.Screen.set_text(str(ret))
        elif Ops.find("*") > 0:
            operandos = Ops.split("*")
            op1 = float(operandos[0])
            op2 = float(operandos[1])
            ret = op1 * op2
            # print(ret)
            self.Screen.set_text(str(ret))
        elif Ops.find("/") > 0:
            operandos = Ops.split("/")
            op1 = float(operandos[0])
            op2 = float(operandos[1])
            if op2 != 0:
                ret = op1 / op2
                self.Screen.set_text(str(ret))
            else:
                self.Screen.set_text("NaN")
            # print(ret)

if __name__ == "__main__":
    Calculadora()

    Gtk.main()