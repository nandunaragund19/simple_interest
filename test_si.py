from si import simpleInt


def test_simpleInt():
    assert simpleInt(1000, 5, 2) == 100


def test_simpleInt rate():
    assert simpleInt(1000, 0, 2) == 0
