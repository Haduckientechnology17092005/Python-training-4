ds = []
for i in range (1000,3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        ds.append(s)
        
print("Even numbers from 1000 to 3000 are : ",','.join(ds))