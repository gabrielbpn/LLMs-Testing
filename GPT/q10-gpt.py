
def is_unique_mastapeece(n, grid):
    # Check if it is even possible to form a mastapeece
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            count_adjacent = 0
            # Check if the current cell is adjacent to 2 tiles of the same color
            if i > 0 and grid[i-1][j] == grid[i][j]:
                count_adjacent += 1
            if i < n - 1 and grid[i+1][j] == grid[i][j]:
                count_adjacent += 1
            if j > 0 and grid[i][j-1] == grid[i][j]:
                count_adjacent += 1
            if j < n - 1 and grid[i][j+1] == grid[i][j]:
                count_adjacent += 1
            if count_adjacent < 2:
                return "NONE"

    # If it's possible to form mastapeece, start filling in the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                grid[i][j] = 'S'
                can_be_glaucous = True
                can_be_sinoper = True
                # Check if it is possible for the current cell to be glaucous
                if i > 0:
                    if grid[i-1][j] == 'S':
                        can_be_glaucous = False
                    if grid[i-1][j] == '.':
                        can_be_glaucous = False
                if i < n - 1:
                    if grid[i+1][j] == 'S':
                        can_be_glaucous = False
                    if grid[i+1][j] == '.':
                        can_be_glaucous = False
                if j > 0:
                    if grid[i][j-1] == 'S':
                        can_be_glaucous = False
                    if grid[i][j-1] == '.':
                        can_be_glaucous = False
                if j < n - 1:
                    if grid[i][j+1] == 'S':
                        can_be_glaucous = False
                    if grid[i][j+1] == '.':
                        can_be_glaucous = False

                # If the cell cannot be glaucous, it has to be sinoper
                if can_be_glaucous == False:
                    grid[i][j] = 'G'

    # Count adjacent tiles of the same color  
    count_s = sum([row.count('S') for row in grid])
    count_g = sum([row.count('G') for row in grid])

    # If the count of adjacent tiles is not equal to 2 for each cell, return "NONE"
    for i in range(n):
        for j in range(n):
            count_adjacent = 0
            if i > 0 and grid[i-1][j] == grid[i][j]:
                count_adjacent += 1
            if i < n - 1 and grid[i+1][j] == grid[i][j]:
                count_adjacent += 1
            if j > 0 and grid[i][j-1] == grid[i][j]:
                count_adjacent += 1
            if j < n - 1 and grid[i][j+1] == grid[i][j]:
                count_adjacent += 1
            if count_adjacent != 2:
                return "NONE"

    # Check if there is a unique mastapeece
    if count_s == count_g:
        return "UNIQUE"
    else:
        return "MULTIPLE"


# Example usage
n1 = 4
grid1 = [
    ['S', '.', '.', '.'],
    ['.', '.', 'G', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', 'S']
]
print(is_unique_mastapeece(n1, grid1))

n2 = 6
grid2 = [
    ['S', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'G', '.', '.'],
    ['.', '.', 'S', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'S'],
    ['.', '.', '.', '.', 'G', '.'],
    ['G', '.', '.', '.', '.', '.']
]
print(is_unique_mastapeece(n2, grid2))

n3 = 10
grid3 = [
    ['.','S','.','.','.','.','S','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','S','S','S','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','G','S','.','.','.','.','.'],
    ['.','.','.','G','.','.','.','.','G','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','G','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.']
]
print(is_unique_mastapeece(n3, grid3))

n4 = 1
grid4 = [['.']]
print(is_unique_mastapeece(n4, grid4))

# WA
# https://codeforces.com/problemset/submission/1586/261452563