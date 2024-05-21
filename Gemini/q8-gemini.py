def find_least_zeros_path(matrix):
  """
  This function finds the path through the matrix with the least trailing zeros
  in the product of its elements.

  Args:
      matrix: A square matrix of non-negative integers.

  Returns:
      A tuple containing the minimum number of trailing zeros and the path string.
  """

  n = len(matrix)
  dp = [[[0, ""] for _ in range(n)] for _ in range(n)]  # dp table for tracking minimum zeros and paths

  # Base cases: starting cell has 0 zeros and empty path
  dp[0][0][0] = 0
  dp[0][0][1] = ""

  # Fill the dp table iteratively
  for i in range(n):
    for j in range(n):
      # Check right movement
      if j + 1 < n and dp[i][j][0] + matrix[i][j + 1].trailing_zeros() <= dp[i][j + 1][0]:
        dp[i][j + 1][0] = dp[i][j][0] + matrix[i][j + 1].trailing_zeros()
        dp[i][j + 1][1] = dp[i][j][1] + "R"
      # Check down movement
      if i + 1 < n and dp[i][j][0] + matrix[i + 1][j].trailing_zeros() <= dp[i + 1][j][0]:
        dp[i + 1][j][0] = dp[i][j][0] + matrix[i + 1][j].trailing_zeros()
        dp[i + 1][j][1] = dp[i][j][1] + "D"

  # Get the minimum zeros and path from the bottom right cell
  min_zeros = dp[-1][-1][0]
  path = dp[-1][-1][1]

  return min_zeros, path

# Get matrix input
n = int(input())
matrix = []
for _ in range(n):
  matrix.append(list(map(int, input().split())))

# Find the path with least zeros
min_zeros, path = find_least_zeros_path(matrix)

# Print the output
print(min_zeros)
print(path)

# RE
# https://codeforces.com/problemset/submission/2/261451318