def max_points(sequence):
  """
  This function calculates the maximum number of points Alex can earn
  by playing his game on a given sequence of integers.

  Args:
      sequence: A list of integers representing Alex's sequence.

  Returns:
      An integer representing the maximum number of points Alex can earn.
  """

  # Create a dictionary to store the count of each number in the sequence.
  count = {}
  for num in sequence:
    count[num] = count.get(num, 0) + 1

  # Calculate the total points by iterating through each number and its neighbors.
  max_points = 0
  for num, num_count in count.items():
    # Add the count of the current number and its neighbors.
    points = num_count
    if num + 1 in count:
      points += count[num + 1]
    if num - 1 in count:
      points += count[num - 1]
    max_points = max(max_points, points)

  return max_points

# Get input
n = int(input())
sequence = list(map(int, input().split()))

# Calculate and print the maximum points
print(max_points(sequence))

# WA
# https://codeforces.com/problemset/submission/455/261451308