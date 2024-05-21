n = int(input())
laptops = []

for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

# Sort laptops by price and then by quality
laptops.sort()

# Check if there are two laptops with different prices but same qualities
found = False

i = 0
j = n - 1

while i < j:
    if laptops[i][0] < laptops[j][0]:
        i += 1
    elif laptops[i][0] > laptops[j][0]:
        j -= 1
    else:
        if laptops[i][1] == laptops[j][1]:
            found = True
            break
        elif laptops[i][1] < laptops[j][1]:
            i += 1
        else:
            j -= 1

if found:
    print("Happy Alex")
else:
    print("Poor Alex")

# WA
# https://codeforces.com/problemset/submission/456/261580457