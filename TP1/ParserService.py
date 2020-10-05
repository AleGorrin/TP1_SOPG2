import socket
import signal
import time
import traceback
import json ,csv
import os
import sys

class CsvReader:
    def __init__(self):
        pass
    def getValues(self):
        csvFilePath = "ejemplo.csv"
        with open(csvFilePath, "r") as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader)
            data = []
            for csvRow in csvReader:
                data.append({"id": csvRow[0], "nombre": csvRow[1], "compra": csvRow[2], "venta": csvRow[3]})
            return json.dumps(data)
       
class Main:

    def __init__(self):
        pass

    def print_msg(self):
        print("Se detecto SIGINT")

    def handler(self, sig, frame):        #defino handler
        print("Signal Number: ", sig, "Frame: ", frame)
        traceback.print_stack(frame)
        self.print_msg()

    def main(self):

        signal.signal(signal.SIGINT, self.handler)

        port = 10000

        try:
            print("Conectado")
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto")
            exit(1)

        checkValue = CsvReader()

        while True:
            try:
                toSendJson = checkValue.getValues()
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(bytearray(toSendJson, 'utf-8'), ('localhost', port))
                time.sleep(30)
            finally:
                print("Error")
                sock.close()

m = Main()
m.main()