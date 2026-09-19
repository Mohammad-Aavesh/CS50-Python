from um import count


def test1():
    assert count("um, um,") == 2
    assert count("um, hello, um, world") == 2
    assert count("um, um, yum,") == 2


def test2():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("um.") == 1
    assert count("um,") == 1


def test3():
    assert count("yum yum") == 0
    assert count("yum") == 0
    assert count("yummy") == 0
