def abbreviate_word(word):
  """
  This function takes a word and returns its abbreviation if the word length is greater than 10 characters.
  Abbreviation format: first letter + number of characters in between + last letter

  Args:
      word: The word to be abbreviated (string)

  Returns:
      The abbreviation of the word (string)
  """
  if len(word) <= 10:
    return word
  else:
    # Extract first and last letter
    abbrev = word[0] + str(len(word) - 2) + word[-1]
    return abbrev

def main():
  """
  This function reads the input, processes each word with the abbreviate_word function, and prints the results.
  """
  num_words = int(input())
  for _ in range(num_words):
    word = input()
    abbreviation = abbreviate_word(word)
    print(abbreviation)

if __name__ == "__main__":
  main()

# AC
# https://codeforces.com/contest/71/submission/261450406
