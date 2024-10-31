import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()

    def initGUI(self):
        uic.loadUi("Interfaz.ui",self)
        self.show()

        self.enviar.clicked.connect(self.imprimir)
    def imprimir(self):
        print("Hola")
         
def main():
    app=PyQt.QApplicacion([])
    window=Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
                                                                                                                                            