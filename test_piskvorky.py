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


def test_tah_hrace():
    # nahradime funkciu input, aby sa nic nepytala uzivatela
    # ignorujeme vstupny parameter funkcie input("...") pomocou _
    original_input = p.input_pre_tah_hrace

    def dummy_input_0(_):
        return 0
    p.input_pre_tah_hrace = dummy_input_0
    assert p.tah_hrace("-----") == "x----"
    assert p.tah_hrace("-ox--") == "xox--"

    def dummy_input_4(_):
        return 4
    p.input_pre_tah_hrace = dummy_input_4
    assert p.tah_hrace("-----") == "----x"
    assert p.tah_hrace("-ox--") == "-ox-x"

    # nemozeme vsak pouzit negativny test, pretoze by sme sa dostali to nekonecneho cyklu
    # def dummy_input_minus1():
    #     return -1

    # vratime vsetko do povodneho stavu, ak treba
    p.input_pre_tah_hrace = original_input


def test_tah_hrace_pre_pokrocilych():
    original_input = p.input_pre_tah_hrace

    # vytvorime iterator z (n-tic) == tuple
    iterator = iter(("a", -1, 20, 0, 2, 1,  # vstup pre 1. volanie p.tah_hrace
                     0,                     # vstup pre 2. volanie p.tah_hrace
                     0))                    # vstup pre 3. volanie p.tah_hrace

    # vytvorime funkciu ktora zavola next vzdy ked volame input
    # posledna hodnota musi byt validna, aby sme predisli nekonecnemu cyklu!!!
    def input_iterator_predefinovanych_hodnot(_):
        return next(iterator)
    p.input_pre_tah_hrace = input_iterator_predefinovanych_hodnot
    assert p.tah_hrace("x-xoo") == "xxxoo"  # pouzi nevalidne hodnoty ("a", -1, 20, 0, 2) a potom 1
    assert p.tah_hrace("--xoo") == "x-xoo"  # pouzi 0, ktora nebola validna pre predosly vstup, ale je validna teraz
    assert p.tah_hrace("-----") == "x----"  # pouzi poslednu 0, tiez validny vstup

    p.input_pre_tah_hrace = original_input


def test_tah_pocitace():
    assert p.tah_pocitace("ox-x") == "oxox"
    # otestuj ci je funkcia dostatocne "random" (zmaz test po implementovani nejakej ne-random strategii)
    bola_pozicia_0 = 0
    bola_pozicia_1 = 0
    bola_pozicia_2 = 0
    for i in range(100):
        tah = p.tah_pocitace("---")
        if tah == "o--":
            bola_pozicia_0 += 1
        elif tah == "-o-":
            bola_pozicia_1 += 1
        elif tah == "--o":
            bola_pozicia_2 += 1
        else:
            raise AssertionError("Ina pozicia: {}".format(tah))
    assert bola_pozicia_0 > 0
    assert bola_pozicia_1 > 0
    assert bola_pozicia_2 > 0
