import numpy as np

matrix = []

print("Nhập các giá trị cho ma trận 3x4:")
def matrix_input():
    for i in range(3):
        row = []
        for j in range(4):
            value = int(input(f"Nhập giá trị cho phần tử ({i},{j}): "))
            row.append(value)
        matrix.append(row)
def matrix_print():
    for i in range(3):
        print(matrix[i][1], end=" ")       
def main(): 
    matrix_input()
    np_matrix = np.array(matrix)
    print("Ma trận đã nhập:")
    print(np_matrix)
    matrix_print()
    # print(np_matrix[0][0])
    # print(np_matrix[2][0])
    # print(np_matrix[2][3])
    print(np_matrix[1])
    print(np_matrix[2])
    
main()
