import pytest
from calculator import add, subtract, multiply, divide

def test_add():
  assert add(10,20) == 35
  
def test_subtract():
  assert subtract(10,20) == -10
