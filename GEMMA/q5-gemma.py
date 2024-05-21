n, m, a, b = map(int, input().split())

total_rides = n // m

if b >= a:
    cost_m_tickets = total_rides * b
    cost_single_tickets = n % m * a
    minimum_cost = min(cost_m_tickets, cost_single_tickets)
else:
    minimum_cost = n * a

print(minimum_cost)



# WA
# https://codeforces.com/problemset/submission/466/261580118