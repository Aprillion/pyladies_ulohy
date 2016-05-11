import piskvorky as p
import pytest


def test_vyhodnot():
    assert p.vyhodnot("xxx----") == "x"
    assert p.vyhodnot("x-ox----") == "-"
    assert p.vyhodnot("xoxoxoxo") == "!"
    assert p.vyhodnot("xxxxxxxx") == "x"
    assert p.vyhodnot("--xx-ooo-") == "o"
    # try:
    with pytest.raises(ValueError):
        p.vyhodnot("12324321a")
    # except ValueError:
    #     assert True
    # else:
    #     assert False


def test_tah():
    assert p.tah("-----", 1, "x") == "-x---"
    assert p.tah("-----", 0, "x") == "x----"
