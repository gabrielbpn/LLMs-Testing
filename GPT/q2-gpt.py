
# Function to abbreviate words with length more than 10 characters
def abbreviate_words(n, words):
    result = []
    for word in words:
        if len(word) > 10:
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
            result.append(abbreviation)
        else:
            result.append(word)
    return result

# Input
n = int(input("Enter the number of words: "))  # The first line contains an integer n
words = []
for i in range(n):
    word = input("Enter word #" + str(i+1) + ": ")  # Each of the following n lines contains one word
    words.append(word)

# Output
result = abbreviate_words(n, words)
for res in result:
    print(res)

# WA
# https://codeforces.com/problemset/submission/71/261452481