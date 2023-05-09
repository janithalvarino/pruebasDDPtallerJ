import pytest
from fastapi import Response as rs 
from main import  verificar_primo 
  

def test_primo():

    assert verificar_primo(5, rs ) == {'respuesta': True, 'validacion': 'Solicitud Exitosa'}

def test_no_primo():
    assert verificar_primo(6, rs) == {'respuesta': False, 'validacion': 'Solicitud Exitosa'} 
    
 