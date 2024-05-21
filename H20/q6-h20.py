# Create a set to store registered usernames
registered_users = set()

def register_user(username):
    """
    Register a new user or generate a new username if it already exists
    """
    if username not in registered_users:
        # Username is available, register it and return OK
        registered_users.add(username)
        return "OK"
    else:
        # Username is taken, generate a new one
        i = 1
        while True:
            new_username = f"{username}{i}"
            if new_username not in registered_users:
                registered_users.add(new_username)
                return new_username
            i += 1

# Read input
n = int(input())
for _ in range(n):
    username = input()
    print(register_user(username))

# TLE
# https://codeforces.com/problemset/submission/4/261453572