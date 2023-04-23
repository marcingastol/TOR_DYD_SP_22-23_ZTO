import pytest
from calculator import add, subtract, multiply, divide

def test_add():
  assert add(10,20) == 30
  
def test_subtract():
  assert subtract(10,20) == -10

def test_multiply():
  assert multiply(10,20) == 200
  
def test_divide():
  assert divide(10,20) == 0.5
