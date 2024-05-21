# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Initialize maximum points and current points
max_points = 0
current_points = 0

# Iterate over the sequence
for i in range(n):
    # Check if this is a step where we can earn more points
    if (i == 0 or sequence[i-1] != sequence[i]) and (i == n-1 or sequence[i+1] != sequence[i]):
        current_points += sequence[i]
        max_points = max(max_points, current_points)
        current_points = 0

# Print the maximum points
print(max_points)

# WA
# https://codeforces.com/problemset/submission/455/261580474