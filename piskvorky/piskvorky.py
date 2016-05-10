""" Hra piskvorky 1D pre http://pyladies.cz/praha/ Lekce 6 - Testování """


def tah(pole, cislo_policka, symbol):
    """vrati pole so symbolom na pozicii"""
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
