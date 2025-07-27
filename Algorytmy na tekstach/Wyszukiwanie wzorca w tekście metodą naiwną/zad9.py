#Zadanie 9.1.
def jak_wystepuje(wzorzec, tekst, m, n):
    czy_moze_z_1_bl = False
    for i in range(len(tekst) - m + 1):
        ile_ok = 0
        for j in range(m):
            if tekst[i + j] == wzorzec[j]:
                ile_ok += 1
        if ile_ok == len(wzorzec):
            return 'dokładnie'
        if ile_ok == len(wzorzec) - 1:
            czy_moze_z_1_bl = True
    if czy_moze_z_1_bl:
        return "z błędem"
    else:
        return 'nie'

T = ['opera', 'aparat', 'karawana', 'bezspornie', 'zakryty', 'solanka']
W = ['para', 'para', 'kran', 'sport', 'ryt', 'sofa']

for w, t in zip(W, T):
    print(w, t, jak_wystepuje(w, t, len(w), len(t)))

#Zadanie 9.2.
#Odpowiedź:
#wzorzec: baba
#babababa

#Zadanie 9.3.
#Odpowiedzią jest funkcja jak_wystepuje() i funkcja czy_wystepuje() zapisana poniżej
def czy_wystepuje(wzorzec, tekst, m, n):
    if jak_wystepuje(wzorzec, tekst, m, n) == 'nie':
        return 'NIE'
    else:
        return 'TAK'