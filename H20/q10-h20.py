def is_valid_mastapeece(grid):
    """
    Check if the given grid is a valid mastapeece
    """
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] != '.':
                count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == grid[i][j]:
                        count += 1
                if count != 2:
                    return False
    return True

def dfs(grid, i, j, color):
    """
    Perform DFS to fill the grid with the given color
    """
    n = len(grid)
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if grid[i][j] == '.':
        grid[i][j] = color
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(grid, i + dx, j + dy, color)

def solve_mastapeece(grid):
    """
    Solve the mastapeece problem
    """
    n = len(grid)
    unique_solution = True
    solution = [['.' for _ in range(n)] for _ in range(n)]

    def dfs_solve(i, j):
        nonlocal unique_solution
        if i == n:
            if is_valid_mastapeece(solution):
                if unique_solution:
                    unique_solution = False
                else:
                    return False
            return True
        if j == n:
            return dfs_solve(i + 1, 0)
        if grid[i][j] != '.':
            solution[i][j] = grid[i][j]
            return dfs_solve(i, j + 1)
        for color in 'SG':
            solution[i][j] = color
            dfs(grid, i, j, color)
            if dfs_solve(i, j + 1):
                return True
            solution[i][j] = '.'
        return False

    dfs_solve(0, 0)
    if unique_solution:
        if is_valid_mastapeece(solution):
            return 'UNIQUE', solution
        else:
            return 'NONE', None
    else:
        return 'MULTIPLE', None

n = int(input())
grid = [list(input()) for _ in range(n)]
result, solution = solve_mastapeece(grid)
print(result)
if result == 'UNIQUE':
    for row in solution:
        print(''.join(row))

# WA
# https://codeforces.com/problemset/submission/1586/261453603