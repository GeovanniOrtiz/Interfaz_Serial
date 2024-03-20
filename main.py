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
        self.ui_main.control1.valueChanged.connect(lambda:self.SetData(1))
        self.ui_main.control2.valueChanged.connect(lambda:self.SetData(2))
        self.ui_main.control3.valueChanged.connect(lambda:self.SetData(3))
        self.ui_main.control4.valueChanged.connect(lambda:self.SetData(4))
        self.ui_main.control5.valueChanged.connect(lambda:self.SetData(5))
        self.ui_main.control6.valueChanged.connect(lambda:self.SetData(6))
        self.ui_main.btn_enviar.released.connect(self.SendData)

        self.dial1 = 0
        self.dial2 = 0
        self.dial3 = 0
        self.dial4 = 0
        self.dial5 = 0
        self.dial6 = 0

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
        serial_comm.send_floats(self.dial1, self.dial2, self.dial3, self.dial4, 25.25, 33.33, 77.35, 66.33, self.dial5, self.dial6)

if __name__ == "__main__":
    app = QApplication([])
    window = Interfaz()
    window.show()
    app.exec()