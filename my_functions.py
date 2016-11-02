# prosim ignoruj prvy riadok a prepis si naozajstny subor my_functions.py (alebo vyvor novy)


def obvod_obdelniku(sirka, vyska):
    "Vrati obvod obdelnika danych rozmeru"
    return 2 * (sirka + vyska)

print(obvod_obdelniku(4, 2))
print(obvod_obdelniku(6, 3))