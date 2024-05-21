def modify_string(string):
    """
    This function modifies the given string as follows:
    - Deletes all the vowels.
    - Inserts a character . before each consonant.
    - Replaces all uppercase consonants with corresponding lowercase ones.

    Args:
        string: The input string.

    Returns:
        The modified string.
    """
    result = ''
    for char in string:
        if char not in 'aeiouAEIOU':
            result += '.' + char.lower()
    return result


if __name__ == '__main__':
    # Read the input string.
    string = input()

    # Modify the string and print the output.
    modified_string = modify_string(string)
    print(modified_string)

# WA
# https://codeforces.com/problemset/submission/118/261580102