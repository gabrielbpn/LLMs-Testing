
# Read the input values
n, m, a, b = map(int, input().split())

# Calculate the minimum cost
min_cost = min(n*a, (n//m)*b + (n%m)*a, ((n+m-1)//m)*b)

# Print the minimum sum in rubles that Ann will need to spend
print(min_cost)

# AC
# https://codeforces.com/problemset/submission/466/261452514