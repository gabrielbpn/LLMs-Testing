
# Define the function to process the input string
def process_string(s):
    # Store the vowels in a variable
    vowels = "AEIOUYaeiouy"
    processed_string = ""
    # Iterate through each character in the input string
    for char in s:
        # If the character is a vowel, skip it
        if char in vowels:
            continue
        else:
            # If the character is a consonant, add a "." before it and convert it to lowercase
            processed_string += "." + char.lower()
    return processed_string

# Get the input string from the user
input_string = input("Enter the input string: ")

# Print the resulting processed string
print(process_string(input_string))

# WA
# https://codeforces.com/problemset/submission/118/261452494