A = [2,19,30,45,100,101,104,103,200,301,257]
B = []
for prime in A:
    s = 0
    for i in range (1, prime):
        if prime % i == 0:
            s = s + 1
    if s == 1:
        B.append(prime)
print("A: ", A)
print("B: ", B)