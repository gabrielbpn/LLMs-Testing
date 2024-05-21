n = int(input())

a = list(map(int, input().split()))

points = 0
for x in a:
    points += max(0, x-1) + max(0, x+1) - 1

print(points)



# WA
# https://codeforces.com/problemset/submission/455/261580135