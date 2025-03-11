import pytest
from src.main import conteoPalabras

# pruebas principal
def test_conteo():
    conteo = "Python es increíble, Python es poderoso! Me encanta Python."
    result = conteoPalabras(conteo)
    assert result == {'python': 3, 'es': 2, 'increíble': 1, 'poderoso': 1, 'me': 1, 'encanta': 1}

#prueba de mayusculas y minusculas 
def test_conteoMayusMin():
    conteo = "PytHON python con CON el mejor"
    result = conteoPalabras(conteo)
    assert result == {'python': 2, 'con':2, 'el':1, 'mejor':1}

# prueba con signos de puntuación
def test_conteoPuntuacion():
    conteo = " Holá, como estas?"
    result = conteoPalabras(conteo)
    assert result == {'holá': 1,'como':1, 'estas':1}

#prueba con espacio vacio
def test_conteoVacio():
    conteo = ""
    result = conteoPalabras(conteo)
    assert result == {}
