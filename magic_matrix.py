def create_magic_square(n):
    if n % 2 == 0:
        raise ValueError("n must be an odd number")
    magic_square = [[0]*n for _ in range(n)]
    num = 1
    i = 0
    j = n//2
    while num <= n**2:
        magic_square[i][j] = num
        num += 1
        newi = (i-1)%n
        newj = (j+1)%n
        if magic_square[newi][newj]:
            i+=1
        else:
            i = newi
            j = newj
    return magic_square
def print_magic_square(square):
    for row in square:
        print(" ".join(f"{x:2d}" for x in row))

n = 5
magic_square = create_magic_square(n)
print_magic_square(magic_square)
