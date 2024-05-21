n = int(input())

grid = [list(input()) for _ in range(n)]

visited = set()

def is_valid(row, col, color):
    if row < 0 or row >= n or col < 0 or col >= n or (row, col) in visited:
        return False
    return True

def solve(row, col, color):
    if row == n and col == n:
        return True
    visited.add((row, col))
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if is_valid(i, j, color) and grid[i][j] != '.' and (i, j) not in visited:
                if solve(i, j, color):
                    return True
    return False

def check_mastapeece():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.' or (not is_valid(i, j, 'S') and not is_valid(i, j, 'G')):
                return 'NONE'
    if solve(0, 0, 'S'):
        return 'UNIQUE'
    return 'MULTIPLE'

print(check_mastapeece())

if check_mastapeece() == 'UNIQUE':
    for i in range(n):
        print(''.join([grid[i][j] for j in range(n)]))



# WA
# https://codeforces.com/problemset/submission/1586/261580153