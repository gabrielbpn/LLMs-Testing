def register_system(names):
    seen_names = set()
    for name in names:
        if name not in seen_names:
            print("OK")
        else:
            i = 1
            while True:
                new_name = f"{name}{i}"
                if new_name not in seen_names:
                    print(new_name)
                    break
                i += 1

n = int(input())
names = [input() for _ in range(n)]
register_system(names)

# WA
# https://codeforces.com/problemset/submission/4/261580469