def min_subway_cost(n, m, a, b):
  """
  This function calculates the minimum cost for Ann's subway rides.

  Args:
      n: Number of rides Ann needs to take.
      m: Number of rides covered by the multi-ride ticket.
      a: Cost of a single ride ticket.
      b: Cost of the multi-ride ticket.

  Returns:
      The minimum cost Ann needs to spend.
  """

  # Calculate the cost using single tickets
  single_ticket_cost = n * a

  # Calculate the cost per ride using the multi-ride ticket
  multi_ride_cost = b / m

  # Check if the multi-ride ticket is cheaper per ride
  if multi_ride_cost < a:
    # Calculate the number of full uses of the multi-ride ticket
    full_uses = n // m
    # Calculate the remaining rides after using multi-ride tickets
    remaining_rides = n % m

    # Calculate the cost of remaining rides using single tickets
    remaining_cost = remaining_rides * a

    # Calculate the total cost using multi-ride tickets
    multi_ride_total = full_uses * b

    # Return the minimum cost between single and multi-ride tickets
    return min(single_ticket_cost, multi_ride_total + remaining_cost)
  else:
    # Single ticket is cheaper, return its cost
    return single_ticket_cost

# Get user input
n, m, a, b = map(int, input().split())

# Calculate and print the minimum cost
minimum_cost = min_subway_cost(n, m, a, b)
print(minimum_cost)

# wa
# https://codeforces.com/problemset/submission/466/261451283