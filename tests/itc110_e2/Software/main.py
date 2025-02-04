from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from UI import Ui_MainWindow
import sys
import serial
import serial.tools.list_ports
port = list((serial.tools.list_ports.comports()))
for p in port :
    print(p)
port = "COM10"
ser = serial.Serial(port,9600,timeout =1)

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.value = ""
       
        for n in range(10):
            getattr(self, f'pushButton_{n}').clicked.connect(
                lambda checked, x=n: self.onNumberClick(x))

        for c in ["send", "clear", "back"]:
            getattr(self, f'pushButton_{c}').clicked.connect(
                lambda checked, x=c: self.onButtonClick(x))

    def onNumberClick(self, num: int):
        print(f"Clicked {num}")
        self.value +=str(num)
        self.label_2.setText(self.value)
        


    def onButtonClick(self, cmd: str):
        if cmd =="clear":
            self.value = ""
            self.label_2.setText(self.value)
        if cmd =="send":
 
                ser.write(self.value.encode(encoding="utf-8"))
                self.value = ""
                self.label_2.setText(self.value)
        print(f"Clicked {cmd}")



app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())