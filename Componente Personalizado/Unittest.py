import unittest

from PySide6.QtWidgets import QApplication, QWidget
from Animado import AnimatedButton

class NamesTestCase(unittest.TestCase):

    

    def test_colorAnimacion(self):
       app=QApplication.instance()
       if app==None:
        app= QApplication([])
       window=QWidget()
       animado = AnimatedButton(color='blue')
       resultado = animado.pcolor
       self.assertEqual(resultado,'blue')

    def test_TextoBoton(self): 
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        window=QWidget()       
        animado = AnimatedButton(textoboton='Limpia')
        resultado= animado.ptexto
        self.assertEquals(resultado,'Limpia')
    
    

if __name__ == '__main__':
    unittest.main()
