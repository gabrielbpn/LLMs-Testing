n = int(input())

prices = [int(input()) for i in range(n)]
qualities = [int(input()) for i in range(n)]

prices.sort()
qualities.sort(reverse=True)

for i in range(n):
    if qualities[i] > qualities[prices.index(prices[i])]:
        print('Happy Alex')
        exit()

print('Poor Alex')



# RE
# https://codeforces.com/problemset/submission/456/261580112