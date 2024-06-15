def max_points(n, arr):
    # Create a frequency mapping of the numbers in the array
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Initialize the maximum points
    max_points = [0] * (max(arr) + 1)
    
    # Calculate the maximum points for each number
    for i in range(max(arr) + 1):
        if i == 0:
            max_points[i] = 0
        elif i == 1:
            max_points[i] = freq.get(1, 0)
        else:
            max_points[i] = max(max_points[i-1], max_points[i-2] + freq.get(i, 0) * i)
    
    return max_points[max(arr)]

# Reading input from user
n = int(input())
arr = list(map(int, input().split()))

# Calling the function and printing the result
print(max_points(n, arr))

# AC
# https://codeforces.com/problemset/submission/455/263073947