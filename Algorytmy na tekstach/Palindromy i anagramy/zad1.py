def czy_palindrom(n, s):
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def czy_anagramy(n1, n2, s1, s2):
    if n1 != n2:
        return False
    else:
        TC1 = [0] * 256
        TC2 = [0] * 256
        for i in range(n1):
            TC1[ord(s1[i])] += 1
            TC2[ord(s2[i])] += 1
        for j in range(97, 123):
            if TC1[j] != TC2[j]:
                return False
        return True

def czy_palindrom2(s):
    return ''.join(reversed(s)) == s

def czy_anagramy2(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))