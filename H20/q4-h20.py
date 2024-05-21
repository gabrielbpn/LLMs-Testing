def check_alex_guess():
    n = int(input())  # read the number of laptops
    laptops = []
    for _ in range(n):
        price, quality = map(int, input().split())  # read price and quality of each laptop
        laptops.append((price, quality))  # store in a list of tuples

    # sort laptops by price
    laptops.sort(key=lambda x: x[0])

    for i in range(n-1):
        if laptops[i][1] > laptops[i+1][1]:
            print("Happy Alex")
            return

    print("Poor Alex")

check_alex_guess()

# ac
# https://codeforces.com/problemset/submission/456/261453549