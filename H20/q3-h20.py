def process_string(s):
    """
    Process the input string according to Petya's task
    """
    vowels = 'AOYEUaiouey'
    result = ''
    for char in s:
        if char not in vowels:
            result += '.' + char.lower()
    return result

# Get the input string from the user
s = input()

# Process the string and print the result
print(process_string(s))

# wa
# https://codeforces.com/problemset/submission/118/261453526