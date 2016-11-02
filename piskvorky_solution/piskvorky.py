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
import random


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


# pouzijme explicitne premennu pre funkciu input, aby sme ju mohli zmenit pri testovani
input_pre_tah_hrace = input


def tah_hrace(pole):
    """11. Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
    a vrátí herní pole se zaznamenaným tahem hráče.
    Funkce by měla odmítnout záporná nebo příliš velká čísla, a tahy na obsazená políčka. Pokud uživatel
    zadá špatný vstup, funkce mu vynadá a zeptá se znova."""
    print("Herni pole: {}".format(pole))
    # TODO: napoveda je pre velkost pola 20. treba upravit na rozne velkosti, idealne v samostatnej funkcii
    print("Cisla poli: 01234567890123456789")
    print("                      1111111111")
    while True:
        znak = input_pre_tah_hrace("Zadej cislo policka 0-19: ")
        try:
            cislo_policka = int(znak)
        except ValueError:
            print("Prosim, zadej cele cislo, ne `{}`.".format(znak))
        else:
            if cislo_policka < 0 or cislo_policka > 19:
                print("Prosim, zadej cislo v rozmedzi 0 az 19 (vcetne).")
            elif pole[cislo_policka] != "-":
                print("Policko {} je obsadene, skus znova.".format(cislo_policka))
            else:
                # implicitne break
                return tah(pole, cislo_policka, "x")


def tah_pocitace(pole):
    """12. Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
    herní pole se zaznamenaným tahem počítače. Použij jednoduchou náhodnou „strategii”:
    1.    Vyber číslo od 0 do 19
    2.    Pokud je dané políčko volné, hrej na něj
    3.    Pokud ne, opakuj od bodu 1"""
    while True:
        cislo_policka = random.randrange(len(pole))
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, "o")


def piskvorky1d():
    """13. Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem, a střídavě volá funkce tah_hrace a
    tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze. Nezapomeň kontrolovat stav hry po každém tahu."""
    pole = "-" * 20
    na_tahu = "x"
    while True:
        if na_tahu == "x":
            pole = tah_hrace(pole)
            na_tahu = "o"
        elif na_tahu == "o":
            pole = tah_pocitace(pole)
            na_tahu = "x"
        vysledek = vyhodnot(pole)
        if vysledek != "-":
            if vysledek == "!":
                print("Remize! {}".format(pole))
            elif vysledek == "x":
                print("Vyhral(a) jsi nad pocitacem! {}".format(pole))
            elif vysledek == "o":
                print("Bohuzel, pocitac vyhral. {}".format(pole))
            else:
                raise ValueError("Necakany vysledek `{}`!?!".format(vysledek))
            return


# spustaci subor je hra.py, aby sme mohli testovat bez spustenia hry.
# alternativne mozme definovat kod ktory sa sice spusti pri spusteni suboru, ale nie pri importovani:
if __name__ == '__main__':
    piskvorky1d()
