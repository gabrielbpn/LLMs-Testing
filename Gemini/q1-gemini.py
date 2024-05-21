def can_divide_watermelon(weight):
  """
  This function checks if the watermelon weight (w) can be divided into two parts with even weights.

  Args:
      weight: The weight of the watermelon (integer)

  Returns:
      "YES" if the division is possible, "NO" otherwise (string)
  """
  # Check if weight is positive
  if weight <= 0:
    return "NO"
  # Check if weight is even
  return "YES" if weight % 2 == 0 else "NO"

def main():
  """
  This function reads the watermelon weight from the input and prints the result.
  """
  watermelon_weight = int(input())
  result = can_divide_watermelon(watermelon_weight)
  print(result)

if __name__ == "__main__":
  main()

# WA
# https://codeforces.com/contest/4/submission/261450263