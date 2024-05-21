
# Function to find the maximum number of points that Alex can earn
def max_points(n, sequence):
    # Create a list with the count of each element in the sequence
    count = [0]*100005
    for i in sequence:
        count[i] += 1
    
    # Create a list to store the maximum points for each element
    dp = [0]*100005
    dp[0] = 0
    dp[1] = count[1]

    # Iterate through the sequence to calculate the maximum points
    for i in range(2, max(sequence)+1):
        dp[i] = max(dp[i-1], dp[i-2] + i*count[i])
    
    # Print the maximum points that Alex can earn
    return dp[max(sequence)]

# Example inputs
print(max_points(2, [1, 2]))  # Output: 2
print(max_points(3, [1, 2, 3]))  # Output: 4
print(max_points(9, [1, 2, 1, 3, 2, 2, 2, 2, 3]))  # Output: 10

# WA
# https://codeforces.com/problemset/submission/455/261452526