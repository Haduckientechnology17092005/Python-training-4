def is_magic_square(matrix):
    n = len(matrix)
    sum_diag1 = sum_diag2 = sum_row = sum_col = 0
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    if sum_diag1 != sum_diag2:
        return False
    for i in range(n):
        sum_row = sum(matrix[i])
        sum_col = sum(matrix[j][i] for j in range(n))
        if sum_row != sum_col:
            return False
    return True

n = int(input("Enter the size of the matrix: "))
matrix = []
def input_matrix(n):
    for i in range(n):
        row = []
        for j in range(n):
            value = int(input(f"Enter value for row {i+1} and column {j+1}: "))
            row.append(value)
        matrix.append(row)
        
def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
        
input_matrix(n)
if is_magic_square(matrix):
    print("Ma trận là ma phương.")
else:
    print("Ma trận không phải là ma phương.")
print_matrix(n)