def can_divide_watermelon(w):
    """
    Returns True if the watermelon can be divided into two parts, each weighing an even number of kilos,
    and False otherwise.
    """
    # If the weight of the watermelon is even, we can divide it into two even parts
    return w % 2 == 0

# Get the input from the user
w = int(input())

# Check if the watermelon can be divided and print the result
if can_divide_watermelon(w):
    print("YES")
else:
    print("NO")

# wa
# https://codeforces.com/problemset/submission/4/261453504