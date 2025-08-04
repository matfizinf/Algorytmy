#Algorytm nr 1 - wersja iteracyjna z odejmowaniem
def NWD1(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

#Algorytm nr 2 - wersja iteracyjna z resztą z dzielenia
def NWD2(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a

#Algorytm nr 3 - wersja rekorencyjna z odejmowaniem
def NWD3(a, b):
    if a != b:
        if a > b:
            return NWD3(a - b, b)
        else:
            return NWD3(a, b - a)
    else:
        return a

#Algorytm nr 3 - wersja rekurencyjna z resztą z dzielenia
def NWD4(a, b):
    if b != 0:
        return NWD4(b, a % b)
    else:
        return a