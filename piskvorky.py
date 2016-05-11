"""
Hra piskvorky 1D pre http://pyladies.cz/praha/ => Lekce 6 - Testován

Zadanie podla http://pyladies.cz/v1/s004-strings/handout/handout4.pdf => uloha 9 a nasledujuce.
"""


def vyhodnot(pole):
    """vrat 'x' ak vyhral hrac x, 'o' ak o, '!' ak je remiza a '-' v inych pripadoch"""
    if pole.replace("x", "").replace("o", "").replace("-", "") != "":
        raise ValueError("pole obsahuje ine znaky ako x, o, -")
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah(pole, cislo_policka, symbol):
    """vrat pole s vymenenym symbolom na cisle policka"""
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
