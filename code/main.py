def suma(a:int, b:int) -> int:
    return a + b

def resta(a:int, b:int) -> int:
    return a - b

def multiplicacion(a:int, b:int) -> int:
    return a * b

def division(a:int, b:int) -> int:
    try:
        return a / b
    except ZeroDivisionError:
        return 1

def modulo(a:int, b:int) -> int:
    return a % b