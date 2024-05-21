def happy_alex(laptops):
  """
  This function checks if there are two laptops where the first one
  is cheaper (strictly lower price) but has higher quality (strictly 
  higher quality value) than the second one.

  Args:
      laptops: A list of tuples, where each tuple represents a laptop
               (price, quality).

  Returns:
      A string, either "Happy Alex" if Alex is correct, or "Poor Alex"
      otherwise.
  """

  # Loop through each laptop (i)
  for i in range(len(laptops)):
    price_i, quality_i = laptops[i]

    # Loop through laptops after the current one (j)
    for j in range(i + 1, len(laptops)):
      price_j, quality_j = laptops[j]

      # Check if Alex's guess is correct
      if price_i < price_j and quality_i > quality_j:
        return "Happy Alex"

  # No laptops found that satisfy Alex's guess
  return "Poor Alex"

if __name__ == "__main__":
  # Get the number of laptops
  n = int(input())

  # Read laptop data
  laptops = []
  for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

  # Check if Alex is happy
  result = happy_alex(laptops)
  print(result)

  # TLE
  # https://codeforces.com/problemset/submission/456/261451279
