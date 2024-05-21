# Request input from user
n = int(input())
words = []
for i in range(n):
    words.append(input())

# Define the function to process each word
def process_word(word):
    if len(word) > 10:
        first_letter = word[0]
        last_letter = word[-1]
        middle_letters = str(len(word) - 2)
        return f"{first_letter}{middle_letters}{last_letter}"
    else:
        return word

# Process each word and print the result
for i, word in enumerate(words):
    print(process_word(word))

# AC
# https://codeforces.com/problemset/submission/71/261580445