n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().strip().split()])

row, col = 0, 0
trailing_zeros = float('inf')
way = []

while row < n and col < n:
    if row == 0 and col == 0:
        trailing_zeros = min(trailing_zeros, matrix[row][col] % 10)
    if row < n - 1:
        new_trailing_zeros = matrix[row][col] % 10 + trailing_zeros
        if new_trailing_zeros < trailing_zeros:
            trailing_zeros = new_trailing_zeros
            way.append('D')
            row += 1
    else:
        way.append('R')
        col += 1

print(trailing_zeros)
print(''.join(way))


# TLE
# https://codeforces.com/problemset/submission/2/261580142