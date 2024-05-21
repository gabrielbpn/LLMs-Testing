def process_string(text):
  """
  This function processes the given text by removing vowels,
  inserting "." before consonants, and converting uppercase consonants
  to lowercase.

  Args:
      text: The input string consisting of uppercase and lowercase Latin letters.

  Returns:
      The processed string.
  """
  vowels = "aeiouAEIOU"
  result = ""
  for char in text:
    if char not in vowels:
      result += "." + char.lower()
  return result

# Get input string from the user
text = input("Enter a string: ")

# Process the string
processed_text = process_string(text)

# Print the result
print(processed_text)

# WA
# https://codeforces.com/contest/118/submission/261451273