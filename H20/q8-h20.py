import heapq

def min_trailing_zeros(matrix):
    n = len(matrix)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 0
    pq = [(0, 0, 0)]  # (trailing zeros, row, col)

    directions = [(0, 1), (1, 0)]  # right, down

    while pq:
        tz, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1:
            break
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                ntz = tz + matrix[nr][nc].bit_length() - 1
                if ntz < dp[nr][nc]:
                    dp[nr][nc] = ntz
                    heapq.heappush(pq, (ntz, nr, nc))

    path = []
    r, c = n - 1, n - 1
    while r > 0 or c > 0:
        if r > 0 and c > 0:
            if dp[r - 1][c] < dp[r][c - 1]:
                path.append('D')
                r -= 1
            else:
                path.append('R')
                c -= 1
        elif r > 0:
            path.append('D')
            r -= 1
        else:
            path.append('R')
            c -= 1
    path.reverse()

    return dp[-1][-1], ''.join(path)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

tz, path = min_trailing_zeros(matrix)
print(tz)
print(path)

# WA
# https://codeforces.com/problemset/submission/2/261453918