import pytest
from PySide6 import QtCore
from Animado import AnimatedButton


@pytest.fixture
def animado(qtbot):
    animado = AnimatedButton()
    qtbot.addWidget(animado)
    return animado

def test_initial_status(animado):
    assert animado.lineEdit.text() == ""

def test_postclick_status(animado,qtbot):
    qtbot.mouseClick(animado.boton, QtCore.Qt.LeftButton)
    assert animado.lineEdit.text() == ""




