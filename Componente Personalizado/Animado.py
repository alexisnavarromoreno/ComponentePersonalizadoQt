from PySide6.QtWidgets import QStackedLayout,QWidget, QLineEdit, QPushButton,QVBoxLayout
from PySide6.QtCore import Property,QEasingCurve, QPropertyAnimation, QPoint, QSize,Qt,QSequentialAnimationGroup


class AnimatedButton(QWidget):
    
    def __init__(self,parent=None, color='black',textoboton='Limpiar'):
        super().__init__(parent)


        self._color= color
        self._textoboton=textoboton

        # Tamaño del widget
        self.setFixedSize(180,70)

        # Creamos el boton, le damos el tamaño y lo conectamos a el método
        self.boton=QPushButton(f'{self._textoboton}')
        self.boton.setFixedSize(QSize(170,20))
        self.boton.clicked.connect(self.FuncionPresionar)

        # Creamos el line edit y le establecemos un tamaño fijo y una alineacion
        self.lineEdit=QLineEdit()
        self.lineEdit.setFixedSize(170,20)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        # Layout principal
        self.layout = QVBoxLayout() 

        # Alineacion del layout principal
        self.layout.setAlignment(Qt.AlignCenter)       
        # Creamos el widget que hará la animación y le aplicamos el estilo y el tamaño      
        self.widget = QWidget()
        self.widget.setStyleSheet(f'background-color: {self._color};border-radius:15px;')
        self.widget.setFixedSize(20,20)
        
        # Creamos un layout para poder apilar el line edit y el widget
        self.layoutStack=QStackedLayout()

        # Añadimos al layout stack el line edit y el widget
        
        self.layoutStack.addWidget(self.lineEdit)      
        self.layoutStack.addWidget(self.widget)
        self.layoutStack.setAlignment(Qt.AlignCenter)   
        
        # Añadimos al layout principal el layout stack
        self.layout.addLayout(self.layoutStack)  
        # Luego añadimos el botón       
        self.layout.addWidget(self.boton)



        # Le establecemos al widget el layout principal
        self.setLayout(self.layout)      
                
        # Creamos la primera animacion
        self.animation = QPropertyAnimation(self.widget, b'pos')
        self.animation.setDuration(1000)
        self.animation.setStartValue(QPoint(20,10))
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setEndValue(QPoint(180, 10))

        # Creamos la segunda animacion
        self.animation2 = QPropertyAnimation(self.widget, b"pos")
        self.animation2.setDuration(1000)
        self.animation2.setStartValue(QPoint(180, 10))
        self.animation2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation2.setEndValue(QPoint(20,10))

        # Creamos el grupo de animaciones y añadimos las dos
        self.animations_group = QSequentialAnimationGroup()
        self.animations_group.addAnimation(self.animation)
        self.animations_group.addAnimation(self.animation2)


        

    
    def getColor(self):
        return self._color
    
    def setColor(self , color):
        self._color = color
    
    def getTextoBoton(self):
        return self._textoboton

    def setTextoBoton(self ,textoBoton):
        self._textoboton= textoBoton


    pcolor = Property(str, getColor, setColor)  
    ptexto = Property(str, getTextoBoton, setTextoBoton) 


    def MetodoFinalizar(self):
        self.lineEdit.setText("")   
        self.layoutStack.setCurrentIndex(0)

    def FuncionPresionar(self):
        self.layoutStack.setCurrentIndex(1)    
        self.animations_group.start()
        self.animations_group.finished.connect(self.MetodoFinalizar)