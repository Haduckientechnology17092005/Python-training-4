import numpy as np
matrix = []
def create_matrix(n):
    for i in range(n):
        row = []
        for j in range(n):
            value = int(input("Enter value : "))
            row.append(value)
        matrix.append(row)

def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
def matrix_main(n):
    for i in range(n):
        print(matrix[i][i], end=" ")
def matran_tamgiactren(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                print(matrix[i][j], end=" ")
                sum = sum + matrix[i][j]
            else:
                print(0, end=" ")
        print()
    print("Tong phan tu tren duong cheo chinh: ", sum)
def matran_tamgiacduoi(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(matrix[i][j], end=" ")
                sum = sum + matrix[i][j]
            else:
                print(0, end=" ")
        print()
    print("Tong phan tu tren duong cheo duoi: ", sum)
def matran_xoanoc(n):
    matrix1 = [[0]*n for _ in range(n)]
    num = 1
    top, bottom = 0, n-1
    left, right = 0, n-1
    while top <= bottom and left<=right:
        for i in range(left, right+1):
            matrix1[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom+1):
            matrix1[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left-1, -1):
            matrix1[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top-1, -1):
            matrix1[i][left] = num
            num += 1
        left += 1
    for i in range(n):
        for j in range(n):
            print(matrix1[i][j], end=" ")
        print()
        
            
            
            
def main():
    n = int(input("Enter number of elements : "))
    # np_matrix = np.array(matrix)
    # print(np_matrix)
    # create_matrix(n)
    # print_matrix(n)
    # print("Duong cheo chinh: ")
    # matrix_main(n)
    # print()
    # print("Ma tran tam giac tren : ")
    # matran_tamgiactren(n)
    # print()
    # matran_tamgiacduoi(n)
    # print()
    print("Ma tran xoanoc : ")
    matran_xoanoc(n)
    return 0

main()
