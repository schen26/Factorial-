import pytest
from files import factorials

def test_factorial_four():
    assert factorials.factorial(24)==4

def test_factorial_five():
    assert factorials.factorial(4)=='NONE'

def test_factorial_one():
    assert factorials.factorial(1)==1
    
def test_factorial_three():
    assert factorials.factorial(3)=='NONE'
