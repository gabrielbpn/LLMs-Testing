
# Read the number of laptops
n = int(input())

# Initialize a list to store the prices and qualities of the laptops
laptops = []

# Read the description of each laptop and store it in the list
for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

# Sort the laptops based on the price
laptops.sort()

# Check if there is a laptop that is cheaper and of higher quality than the next one
for i in range(n - 1):
    if laptops[i][0] < laptops[i + 1][0] and laptops[i][1] > laptops[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")

# AC
# https://codeforces.com/problemset/submission/456/261452502