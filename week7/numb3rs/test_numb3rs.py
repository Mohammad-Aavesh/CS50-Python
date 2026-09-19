from numb3rs import validate

def test_length():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1") == False
    assert validate("1.") == False
    assert validate("1.1.1.1.1") == False

def test_values():
    assert validate("225.225.225.225") == True
    assert validate("256.256.256.256") == False
    assert validate("1000.100.10.1") == False
    assert validate("1.01.010.001") == False
    assert validate("cats.dogs") == False
