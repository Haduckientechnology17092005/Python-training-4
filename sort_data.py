A = [('John','20','91'),('Rick','19','80'),('Jen','22','85'),('Jen','21','90'), ("Kien","19","100")]
def last(n):
    return (n[0], int(n[1])), int(n[2])
def sort_list(tuples):
    return sorted(tuples, key=last)
print(sort_list(A))