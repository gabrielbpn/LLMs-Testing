
# define a function to find the least round way
def least_round_way(n, matrix):
    # create a 2D list to store number of trailing zeros and the way itself
    dp = [[0] * n for _ in range(n)]
    
    # fill the dp table from bottom-right to upper-left
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == n-1 and j == n-1:
                dp[i][j] = (0, '')  # initialize the bottom-right cell
            else:
                # check the number of trailing zeros when moving right
                right_zeros, right_way = (dp[i][j+1][0] + (matrix[i][j+1] == 0), 'R' + dp[i][j+1][1])
                
                # check the number of trailing zeros when moving down
                down_zeros, down_way = (dp[i+1][j][0] + (matrix[i+1][j] == 0), 'D' + dp[i+1][j][1])
                
                # choose the direction with the least number of trailing zeros
                if right_zeros < down_zeros:
                    dp[i][j] = (right_zeros, right_way)
                else:
                    dp[i][j] = (down_zeros, down_way)
    
    # return the least number of trailing zeros and the way itself
    return dp[0][0]

# get input from user
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# call the function and store the result
num_zeros, way = least_round_way(n, matrix)

# output the result
print(num_zeros)
print(way)

# RE
# https://codeforces.com/problemset/submission/2/261452549