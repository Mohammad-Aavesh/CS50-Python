from plates import is_valid

def test_string_True():
    assert is_valid("Hello") == True
    assert is_valid("Hello, world") == False

def test_alphanumeric_True():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50.") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50C") == False

def test_numbers():
    assert is_valid("12340") == False

def test_length():
    assert is_valid("F") == False
    assert is_valid("HelloWorld") == False
    assert is_valid("FON") == True
