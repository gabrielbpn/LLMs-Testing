# Get input from user
n, m, a, b = map(int, input().split())

# Calculate minimum sum of money needed
min_sum = 0
while n > 0:
    if n >= m:
        min_sum += b
        n -= m
    else:
        min_sum += a
        n -= 1

print(min_sum)

# WA
# https://codeforces.com/problemset/submission/466/261580463