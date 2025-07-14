s = 'konstantynopolitanczykiewiczowianeczka'
n = len(s)

#Algorytm nr 1 - z wykorzystaniem tablicy częstości

TC = [0] * 256

for i in range(n):
    TC[ord(s[i])] += 1

print(TC)

#Algorytm nr 2 - z wykorzystaniem mapy

MC = {}

for i in range(n):
    if s[i] in MC:
        MC[s[i]] += 1
    else:
        MC[s[i]] = 1

print(MC)