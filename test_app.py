from app import add , subtract

def test_add():
    assert add(10,5) == 15

def test_sub():
    assert subtract(10,5) == 5

def test_mul(a=10,b=20):
    return a*b
