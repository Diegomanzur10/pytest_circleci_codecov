from code.main import suma, resta, multiplicacion, division, modulo
import pytest

@pytest.mark.parametrize(
    (
        "a",
        "b",
        "val_exp"
    ),
    [
        (
            2,
            2,
            4
        ),
        (
            3,
            5,
            8
        )
    ],
    ids = [
        "Test1",
        "Test2"
    ]
)
def test_suma(a, b, val_exp):
    assert suma(a, b) == val_exp

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6

@pytest.mark.xfail(reason = "Funcion a depricar")
def test_division():
    assert division(3, 0) == 1