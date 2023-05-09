import pytest
from fastapi import Response as rs 
from main import  fibonacci


def test_fibonacci():
    assert fibonacci(5 , rs) == {"validacion": "Solicitud Exitosa", "respuesta":5 }  
