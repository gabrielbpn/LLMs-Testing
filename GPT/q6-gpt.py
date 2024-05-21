
# create a dictionary to store the usernames and their occurrences
username_database = {}

# function to check if the username exists in the database, if it does, update the count and return the new username
def register_user(username):
    if username in username_database:
        username_database[username] += 1
        prompt = username + str(username_database[username])
        username_database[prompt] = 0
        return prompt
    else:
        username_database[username] = 0
        return "OK"

# read the number of requests
n = int(input())

# iterate through the requests and display the response
for _ in range(n):
    request = input()
    response = register_user(request)
    print(response)

# AC
# https://codeforces.com/problemset/submission/4/261452521