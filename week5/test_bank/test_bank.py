from bank import value

def test_hello():
    assert value("hello") == 0

def test_case():
    assert value("Hello") == 0

def test_wordH():
    assert value("Hi") == 20

def test_phrase():
    assert value("What's up") == 100
