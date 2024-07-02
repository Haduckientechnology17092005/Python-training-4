p = []
n  = int(input("Enter number of elements : "))
dem = 0
nguyen_to = 2
while dem < n:
    s = 0
    for k in range (1, nguyen_to):
        if nguyen_to % k == 0:
            s = s + 1
    if s == 1:
        p = p + [nguyen_to]
    dem = dem+1
    nguyen_to = nguyen_to + 1
print("Prime numbers in the list are : ",n," : ",p)