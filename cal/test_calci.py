# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
def add(a,b):
    return a+b 
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 0
    return a/b


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5
    assert div(10, 0) == 0
