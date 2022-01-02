import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Animado import AnimatedButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Animado")
        self.setFixedSize(190,80)       
        animado = AnimatedButton()
        self.setCentralWidget(animado)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
