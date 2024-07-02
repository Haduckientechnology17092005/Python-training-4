ds = []
n =  int(input("Enter number of elements : "))
for i in range (n):
    dat = int(input("Enter number : "))
    ds.append(dat)
lonnhat = ds[0]
nhonhat = ds[0]
for i in range(n):
    if lonnhat < ds[i]:
        lonnhat = ds[i]
    if nhonhat > ds[i]:
        nhonhat = ds[i]
print("Max number is : ",lonnhat)
print("Min number is : ",nhonhat)