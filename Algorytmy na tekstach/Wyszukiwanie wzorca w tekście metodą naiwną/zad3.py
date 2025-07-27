dane = [[[0 for _ in range(8)] for _ in range(8)] for _ in range(125)]

plik = open('szachy.txt')

for i in range(125):
    for j in range(8):
        wiersz = plik.readline().strip()
        for k in range(8):
            dane[i][j][k] = wiersz[k]
    plik.readline()

print(dane)

wzorce1 = ['kW', 'k.W', 'k..W', 'k...W', 'k....W', 'k.....W', 'k......W']
wzorce2 = ['Kw', 'K.w', 'K..w', 'K...w', 'K....w', 'K.....w', 'K......w']

szach_kW = [False] * 125
szach_Kw = [False] * 125

for i in range(125):
    for j in range(8):
        wiersz = ''.join(dane[i][j])
        kolumna = ''.join([dane[i][k][j] for k in range(8)])
        print(wiersz, kolumna)
        for k in range(len(wzorce1)):
            if wzorce1[k] in wiersz or wzorce1[k] in wiersz[::-1] or wzorce1[k] in kolumna or wzorce1[k] in kolumna[::-1]:
                szach_kW[i] = True
            if wzorce2[k] in wiersz or wzorce2[k] in wiersz[::-1] or wzorce2[k] in kolumna or wzorce2[k] in kolumna[::-1]:
                szach_Kw[i] = True

print(sum(szach_kW), sum(szach_Kw))