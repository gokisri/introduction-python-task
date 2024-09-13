def extract_words(s):
    # Split the string into words based on whitespace
    words = s.split()
    return words

# Example usage
input_string = input("Enter a string: ")
words = extract_words(input_string)
print("The words in the string are:", words)
