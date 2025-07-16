def czy_palindrom2(s):
    return ''.join(reversed(s)) == s

def reg(w):
    if len(w) == 1:
        return 1
    else:
        if not czy_palindrom2(w):
            return 0
        else:
            w1 = w[:len(w)//2]
            return reg(w1) + 1

W = ['BABBAB', 'BABBBB', 'BAAAAB', 'B', 'BBB', 'AAAAAAAA']

'''for w in W:
    print(w, reg(w))'''

#Zadanie 4.2.
def REG(w, n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            m = n // 2
        else:
            m = (n - 1) // 2
        for i in range(m):
            if w[i] != w[n - 1 - i]:
                return 0
        x = w[:m]
        return 1 + REG(w, m)

for w in W:
    print(w, REG(w, len(w)))