def register_user(name, users):
  """Registers a user with the given name.

  Args:
      name: The name the user wants to register with.
      users: A set of existing usernames.

  Returns:
      A string containing either "OK" for successful registration or a new
      username if the name already exists.
  """
  if name not in users:
    users.add(name)
    return "OK"
  else:
    i = 1
    new_name = name + str(i)
    while new_name in users:
      i += 1
      new_name = name + str(i)
    users.add(new_name)
    return new_name

# Get number of requests
n = int(input())

# Initialize set to store existing usernames
users = set()

# Process each request
for _ in range(n):
  name = input().strip()
  response = register_user(name, users)
  print(response)

# TLE
# https://codeforces.com/problemset/submission/4/261451299
