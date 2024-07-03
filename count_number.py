def count_number_series_greater_than_zero_max(lst):
    count = 0
    temp = []
    for i in lst:
        if i > 0:
            count += 1
        else:
            if count > 0:
                temp.append(count)
            count = 0
    if count > 0:
        temp.append(count)
    max_array = max(temp)
    print(temp)
    return max_array
def max_array(lst):
    return max(lst)
lst = [1, 2, 3, 4, -4, 5, 6, 7, -8, 0, 4, 5, 6, -8, -6,8]
print("Chuoi dai nhat trong mang lon hon 0 la: ",count_number_series_greater_than_zero_max(lst))