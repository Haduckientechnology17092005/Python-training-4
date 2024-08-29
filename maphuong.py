def generate_magic_square_4x4():
    n = 4
    magic_square = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i < n // 4 or i >= 3 * n // 4) and (j < n // 4 or j >= 3 * n // 4):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]
            elif (i >= n // 4 and i < 3 * n // 4) and (j >= n // 4 and j < 3 * n // 4):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]
    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(f"{x:2d}" for x in row))

magic_square = generate_magic_square_4x4()
print_magic_square(magic_square)



