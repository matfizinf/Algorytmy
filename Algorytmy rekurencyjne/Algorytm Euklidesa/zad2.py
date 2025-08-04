dane = [int(w) for w in open('liczby_nwd.txt').readlines()]

#Wersja 1 - z wykorzystaniem funkcji gcd() z modułu math

from math import gcd

print(gcd(*dane))

#Wersja 2 - z wykorzystaniem jednego z algorytmów

def NWD(a, b):
    if b != 0:
        return NWD(b, a % b)
    else:
        return a

def NWD_lista(lista):
    b = lista[0]
    for a in lista:
        b = NWD(a, b)
    return b

print(NWD_lista(dane))