# NB location of python files
# NB naming conventions for test_files
from SomeProg import divide

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide2():
    assert divide(3,2) == 1.0

