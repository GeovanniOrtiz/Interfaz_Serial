import serial
import struct
import time

class SerialCommunication:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate, timeout=None)

    def send_floats(self, *floats):
        # Empaquetar los números flotantes
        data_to_send = struct.pack(f'>{len(floats)}f', *floats)

        # Enviar byte de inicio
        self.ser.write(bytes([255]))

        # Enviar datos
        self.ser.write(data_to_send)

        # Leer datos de vuelta desde Arduino
        received_data = self.ser.read(len(floats) * 4)  # Cada número flotante es de 4 bytes

        # Interpretar los datos recibidos
        unpacked_data = struct.unpack(f'>{len(floats)}f', received_data)

        # Formatear la salida para mostrar solo dos decimales
        formatted_data = [f'{value:.2f}' for value in unpacked_data]

        # Imprimir los datos recibidos
        print("Data received from Arduino:", formatted_data)