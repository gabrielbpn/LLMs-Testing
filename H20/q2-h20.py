def abbreviate_words():
    """
    Reads n words from the input, abbreviates each word if it's too long, and prints the results.
    """
    n = int(input())  # Read the number of words
    for _ in range(n):
        word = input()  # Read a word
        if len(word) > 10:  # Check if the word is too long
            # Calculate the number of letters between the first and last letters
            num_letters = len(word) - 2
            # Create the abbreviation
            abbreviation = f"{word[0]}{num_letters}{word[-1]}"
            print(abbreviation)  # Print the abbreviation
        else:
            print(word)  # Print the original word if it's not too long

abbreviate_words()  # Call the function to start the program

# ac
# https://codeforces.com/problemset/submission/71/261453518