import json

from PySide6.QtWidgets import QMainWindow, QApplication
from Serial import *
from Gui_gui import Ui_MainWindow

# Definir el puerto serial
SERIAL_PORT = 'COM5'

# Crear una instancia de SerialCommunication
serial_comm = SerialCommunication(SERIAL_PORT)

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main =Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.load_state()  # Carga el estado anterior al iniciar la aplicación

        self.ui_main.control1.valueChanged.connect(lambda:self.SetData(1))
        self.ui_main.control2.valueChanged.connect(lambda:self.SetData(2))
        self.ui_main.control3.valueChanged.connect(lambda:self.SetData(3))
        self.ui_main.control4.valueChanged.connect(lambda:self.SetData(4))
        self.ui_main.control5.valueChanged.connect(lambda:self.SetData(5))
        self.ui_main.control6.valueChanged.connect(lambda:self.SetData(6))
        self.ui_main.btn_enviar.released.connect(self.SendData)

    def load_state(self):
        try:
            with open('estado_variables.json', 'r') as file:
                data = json.load(file)
                self.dial1 = data.get('dial1', 0)
                self.dial2 = data.get('dial2', 0)
                self.dial3 = data.get('dial3', 0)
                self.dial4 = data.get('dial4', 0)
                self.dial5 = data.get('dial5', 0)
                self.dial6 = data.get('dial6', 0)

                self.ui_main.lcdNumber.display(self.dial1)
                self.ui_main.lcdNumber_2.display(self.dial2)
                self.ui_main.lcdNumber_3.display(self.dial3)
                self.ui_main.lcdNumber_4.display(self.dial4)
                self.ui_main.lcdNumber_5.display(self.dial5)
                self.ui_main.lcdNumber_6.display(self.dial6)

                self.ui_main.control1.setValue(self.dial1)
                self.ui_main.control2.setValue(self.dial2)
                self.ui_main.control3.setValue(self.dial3)
                self.ui_main.control4.setValue(self.dial4)
                self.ui_main.control5.setValue(self.dial5)
                self.ui_main.control6.setValue(self.dial6)



        except FileNotFoundError:
            # Si el archivo no existe, se creará con valores predeterminados en 0
            #self.dial1 = self.dial2 = self.dial3 = self.dial4 = self.dial5 = self.dial6 = 0
            self.save_state()  # Guarda los valores predeterminados en el archivo

    def save_state(self):
        data = {
            'dial1': self.dial1,
            'dial2': self.dial2,
            'dial3': self.dial3,
            'dial4': self.dial4,
            'dial5': self.dial5,
            'dial6': self.dial6
        }
        with open('estado_variables.json', 'w') as file:
            json.dump(data, file)

    def SetData(self, data):
        match (data):
            case 1:
                self.dial1 = self.ui_main.lcdNumber.value()
            case 2:
                self.dial2 = self.ui_main.lcdNumber_2.value()
            case 3:
                self.dial3 = self.ui_main.lcdNumber_3.value()
            case 4:
                self.dial4 = self.ui_main.lcdNumber_4.value()
            case 5:
                self.dial5 = self.ui_main.lcdNumber_5.value()
            case 6:
                self.dial6 = self.ui_main.lcdNumber_6.value()

            # Envía los datos utilizando los valores guardados
        #serial_comm.send_floats(self.dial1, self.dial2, self.dial3, self.dial4, 25.25, 33.33, 77.35, 66.33, self.dial5, self.dial6)
    def SendData(self):
        self.save_state()  # Guarda el estado después de actualizar las variables
        serial_comm.send_floats(self.dial1, self.dial2, self.dial3, self.dial4, 25.25, 33.33, 77.35, 66.33, self.dial5, self.dial6)

if __name__ == "__main__":
    app = QApplication([])
    window = Interfaz()
    window.show()
    app.exec()