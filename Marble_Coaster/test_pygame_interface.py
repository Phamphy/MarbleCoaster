import pytest
from pygame_interface import resolution

def test_resolution():
    assert resolution([],[0,0],3)==True
    assert resolution([[0,0],[5,5]],[5,3],3)==False
    assert resolution([[0,0],[5,5]],[10,1],3)==True


