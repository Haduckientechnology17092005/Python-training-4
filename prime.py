def prime_numbers_before(n):
    for i in range(2, n):
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)

n = int(input("Enter the number : "))
prime_numbers_before(n)