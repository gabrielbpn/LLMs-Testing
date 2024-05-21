def min_subway_cost(n, m, a, b):
    """
    Calculate the minimum sum of money Ann needs to spend to make n rides.
    """
    # Calculate the cost of buying one ride tickets for all n rides
    one_ride_cost = n * a
    
    # Calculate the number of m ride tickets needed
    m_ride_tickets_needed = n // m
    
    # Calculate the remaining rides not covered by m ride tickets
    remaining_rides = n % m
    
    # Calculate the cost of buying m ride tickets and one ride tickets for remaining rides
    m_ride_cost = m_ride_tickets_needed * b + remaining_rides * a
    
    # Return the minimum cost
    return min(one_ride_cost, m_ride_cost)

# Get input from user
n, m, a, b = map(int, input().split())

# Calculate and print the minimum cost
print(min_subway_cost(n, m, a, b))

# wa
# https://codeforces.com/problemset/submission/466/261453563