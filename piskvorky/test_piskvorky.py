import piskvorky as p


def test_tah():
    assert p.tah("-----", 1, "x") == "-x---"
    assert p.tah("-----", 0, "x") == "x----"
