def additionner(a, b):
    """Effectue une addition entre deux nombres a et b."""
    return a + b

def soustraire(a, b):
    """Retranche le nombre b au nombre a."""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres a et b."""
    return a * b

def diviser(a, b):
    """Divise le nombre a par le nombre b."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro interdite")
    return a / b
