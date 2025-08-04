#Zadania 4.1. i 4.2.
def RozszerzonyEuklides(a, b):
    print(a, b)
    if b != 0:
        (x, y) = RozszerzonyEuklides(b, a % b)
        print(x, y)
        return (y, x - (a // b) * y)
    else:
        return (1, 0)

print(*RozszerzonyEuklides(188, 12))