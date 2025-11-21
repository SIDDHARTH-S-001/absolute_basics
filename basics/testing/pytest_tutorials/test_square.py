import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert num * num == 40

def test_greater():
    num = 100
    assert num > 100

def test_greater_equal():
    num = 100
    assert num >= 100

def test_less():
    num = 100
    assert num < 200

def tesequality():
    assert 10 == 11