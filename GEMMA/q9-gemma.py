import collections

n = int(input())
c = list(map(int, input().split()))

edges = []
for i in range(n - 1):
    x, y = map(int, input().split())
    edges.append((x, y))

def dominatingColor(v):
    colorCount = collections.Counter()
    for u in range(1, v + 1):
        colorCount[c[u]] += 1
    return colorCount.most_common(1)[0][0]

result = [0] * (n + 1)
for v in range(1, n + 1):
    for u in range(1, v + 1):
        if dominatingColor(u) == c[v]:
            result[v] += 1

for res in result:
    print(res)


# RE
# https://codeforces.com/problemset/submission/600/261580147