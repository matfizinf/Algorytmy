def wyszukiwanie_wzorca(s, n, w, m):
    I = []
    for i in range(n - m + 1):
        czy_wzorzec = True
        for j in range(m):
            if s[i + j] != w[j]:
                czy_wzorzec = False
                break
        if czy_wzorzec:
            I.append(i)
    return I

s = 'qwerkotqwerkotjhgkott'
n = len(s)
w = 'kot'
m = len(w)

print(wyszukiwanie_wzorca(s, n, w, m))

#Złożoność: O(n * m)