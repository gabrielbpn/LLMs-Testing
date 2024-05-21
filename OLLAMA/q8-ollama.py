def find_path(matrix):
    n = len(matrix)
    path = ''
    count_zeros = 0
    
    # Start in the upper left cell
    i, j = 0, 0
    
    while i < n and j < n:
        path += 'DR'[j == n - 1]
        if matrix[i][j] == 0:
            count_zeros += 1
        j += (j + 1) % n
        i += int((j + 1) / n)
    
    return count_zeros, path

n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
count_zeros, path = find_path(matrix)

print(count_zeros)
print(path)

# WA
# https://codeforces.com/problemset/submission/2/261580480
