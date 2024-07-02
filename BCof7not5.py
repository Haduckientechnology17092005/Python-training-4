ds = []
for i in range (270, 650):
    if(i%7 == 0 and i%5 !=0):
        ds.append(str(i))
print("Numbers from 270 to 650 that are divisible by 7 but not by 5 are : ",','.join(ds))
