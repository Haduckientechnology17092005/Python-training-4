tp = (1,2,3,4,5,6,7,8,9,10,11)
ds = list()
for i in tp:
    if tp[i-1]%2 != 0:
        ds.append(tp[i-1])
tp_a = tuple(ds)
print("Tuple : ",tp_a)