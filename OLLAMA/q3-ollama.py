def process_string(s):
    result = ""
    for c in s:
        if c.lower() in "aeiouy":
            continue
        else:
            result += "." + c.lower()
    return result

s = input()
print(process_string(s))

# AC
# https://codeforces.com/problemset/submission/118/261580450