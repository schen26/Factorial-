import pytest

import factorial_code

def factorial_test():
    assert factorial_code.factor(120) == 4
    assert factorial_code.factor(150) == "Cannot be factorised"
