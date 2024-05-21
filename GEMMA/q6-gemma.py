n = int(input())

names = set()

for i in range(n):
    name = input()
    if name not in names:
        print("OK")
        names.add(name)
    else:
        count = 1
        while name + str(count) in names:
            count += 1
        print(name + str(count))
        names.add(name + str(count))


# TLE
# https://codeforces.com/problemset/submission/4/261580131