import pytest
from fastapi import Response as rs 
from main import  index 


def test_helloFastApi():

    assert index() == {"mensaje": "Hello FastAPI"}
    
 