def find_saddle_points(matrix):
    saddle_points = []
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    for i in range(num_rows):
        max_value = max(matrix[i])
        max_indices = [j for j in range (num_cols) if matrix[i][j] == max_value]
        for j in max_indices:
            if(all(matrix[k][j] >= matrix[i][j] for k in range(num_rows))):
                saddle_points.append((i, j))
    return saddle_points

# Ma trận bạn cung cấp
matrix = [
    [3, 10, 21, 2],
    [12, 5, 16, 8],
    [1, 9, 30, 14]
]

saddle_points = find_saddle_points(matrix)

if saddle_points:
    print("Các điểm yên ngựa của ma trận là:")
    for point in saddle_points:
        print(f"Vị trí: {point}, Giá trị: {matrix[point[0]][point[1]]}")
else:
    print("Không có điểm yên ngựa trong ma trận.")
