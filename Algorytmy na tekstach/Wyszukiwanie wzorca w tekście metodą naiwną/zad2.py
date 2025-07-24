def czy_k_podobne(n, A, B, k):
    czy_ok = True
    for i in range(k):
        if A[i] != B[n - k + i]:
            czy_ok = False
            break
    if czy_ok:
        for i in range(n - k):
            if A[k + i] != B[i]:
                czy_ok = False
                break
    return czy_ok

#Zadanie 2.1.
A = [[5, 7, 9], [4, 7, 1, 4, 5], [10, 9, 12, 10, 9], [3, 6, 5, 1, 8], [1, 2, 3, 4, 5],
     [1,1,1,1,3,1,1,1,1], [4, 2, 4, 4, 2, 6]]

B = [[5, 7, 9], [1, 4, 5, 4, 7], [10, 10, 9, 9, 12], [5, 1, 8, 3, 6], [3, 4, 5, 1, 2],
     [3,1,1,1,1,1,1,1,1], [4, 4, 2, 6, 4, 2]]

K = [0, 2, 3, 4, 2, 4, 1]

for a, b, k in zip(A, B, K):
    print(czy_k_podobne(len(a), a, b, k))

#Zadanie 2.2.
#wykonane w postaci funkcji czy_k_podobne()

#Zadanie 2.3.
def czy_podobne(n, A, B):
    for k in range(n):
        if czy_k_podobne(n, A, B, k):
            return True
    return False

