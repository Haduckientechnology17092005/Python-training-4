def is_magic_square(matrix):
    n = len(matrix)
    
    # Tính tổng của đường chéo chính
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    
    # Tính tổng của đường chéo phụ
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    
    # Kiểm tra xem hai đường chéo có cùng tổng không
    if sum_diag1 != sum_diag2:
        return False
    
    # Kiểm tra từng hàng và từng cột
    for i in range(n):
        sum_row = sum(matrix[i])
        sum_col = sum(matrix[j][i] for j in range(n))
        
        # Kiểm tra xem tổng của hàng và cột có bằng với tổng của đường chéo chính không
        if sum_row != sum_diag1 or sum_col != sum_diag1:
            return False
    
    # Nếu tất cả các điều kiện trên đều thỏa mãn, thì đây là ma phương
    return True

# Ví dụ về ma trận bậc lẻ
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