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
        self.ui_main.dial.valueChanged.connect(self.SendData)

    def SendData(self):
        dial = self.ui_main.lcdNumber.value()
        serial_comm.send_floats(1.236589, 4.5636, 6.2588, 100, 25.25, 33.33, 77.35, 66.33, 888, dial)

if __name__ == "__main__":
    app = QApplication([])
    window = Interfaz()
    window.show()
    app.exec()