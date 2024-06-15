def replace_long_words(n, words):
    result = []
    for word in words:
        if len(word) > 10:
            abbreviation = word[0] + str(len(word)-2) + word[-1]
            result.append(abbreviation)
        else:
            result.append(word)
    return result

# Read the input n
n = int(input())

# Read the n words
words = []
for _ in range(n):
    word = input()
    words.append(word)

# Call the replace_long_words function and print the result
for word in replace_long_words(n, words):
    print(word)

# AC
# https://codeforces.com/problemset/submission/71/263073079