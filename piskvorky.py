"""
Hra piskvorky 1D http://pyladies.cz/v1/s004-strings/handout/handout4.pdf => úkol 9 a nasl.:

1-D piškvorky se hrají na řádku s dvaceti políčky.
Hráči střídavě přidávají kolečka (o) a křížky (x), třeba:
1. kolo: -------x------------
2. kolo: -------x--o---------
3. kolo: -------xx-o---------
4. kolo: -------xxoo---------
5. kolo: ------xxxoo---------
Hráč, která dá tři své symboly vedle sebe, vyhrál.


Moduly podle http://pyladies.cz/v1/s005-modules/handout/handout5.pdf úkol 0:

Rozděl1DPiškvorkynačtyřimoduly:
• ai.py, kde bude funkce tah_pocitace
• piskvorky.py, kde budou ostatní funkce
• hra.py, kde bude import a volání hlavní funk cez piskvorky.py (a nic jiného)
• test_piskvorky.py, kde budou testy
"""


def vyhodnot(pole):
    """9. Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek, a vrátí jednoznakový řetězec
    podle stavu hry:
    "x" – Vyhrál hráč s křížky (pole obsahuje xxx)
    "o" – Vyhrál hráč s kolečky (pole obsahujeooo)
    "!" – Remíza (pole neobsahuje - , a nikdo nevyhrál)
    "-" – Ani jedna ze situací výše"""
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
    """10. Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí
    herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici."""
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole):
    """11. Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
    a vrátí herní pole se zaznamenaným tahem hráče.
    Funkce by měla odmítnout záporná nebo příliš velká čísla, a tahy na obsazená políčka. Pokud uživatel
    zadá špatný vstup, funkce mu vynadá a zeptá se znova."""
    print("Herni pole: {}".format(pole))
    cislo_policka = int(input("Cislo policka 0-19: "))
    return tah(pole, cislo_policka, "x")


def tah_pocitace():
    """12. Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
    herní pole se zaznamenaným tahem počítače. Použij jednoduchou náhodnou „strategii”:
    1.    Vyber číslo od 0 do 19
    2.    Pokud je dané políčko volné, hrej na něj
    3.    Pokud ne, opakuj od bodu 1"""
    pass


def piskvorky1d():
    """13. Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem, a střídavě volá funkce tah_hrace a
    tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze. Nezapomeň kontrolovat stav hry po každém tahu."""
    pass

# spustaci subor je hra.py, aby sme mohli testovat bez spustenia hry.
# alternativne mozme definovat kod ktory sa sice spusti pri spusteni suboru, ale nie pri importovani:
if __name__ == '__main__':
    # TODO: odkomentuj po implementacii poslednej funkcie
    # piskvorky1d()
    print(tah_hrace("-" * 20))
