

import pytest

def secti(a, b):
    if (isinstance(a, (int, float, complex)) and
        isinstance(b, (int, float, complex))):
        return a + b
    else:
        raise TypeError("nie je cele cislo")

def test_secti():
    assert secti(1, 3) == 4
    assert secti(1, 2) == 3
    assert secti(1.5, 3.5) == 5
    assert secti(-1, -3) == -4
    with pytest.raises(TypeError):
         secti("a", "b")
#     try:
#         secti("a", "b")
#     except TypeError:
#         assert True
#     else:
#         assert False