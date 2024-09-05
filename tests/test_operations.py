from src.math_operations import add,sub

def test_add():
    assert add(4,5)==9
    assert add(-1,1)==0

def test_sub():
    assert sub(3,6)==3
    assert sub(8,5)==-3