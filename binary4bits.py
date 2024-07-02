Li = []
items = [x for x in input("Enter the numbers : ").split()]
for p in items:
    intp = int(p,2)
    if not intp%5:
        Li.append(p)

print("Binary numbers that are divisible by 5 are : ",",".join(Li))