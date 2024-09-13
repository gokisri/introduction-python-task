def count_unique_characters(x):
    # Create a set from the string, which removes duplicate characters
    unique_chars = set(x)
    
    # Return the number of unique characters
    return len(unique_chars)

# Example usage
input_string = input("Enter a string: ")
unique_count = count_unique_characters(input_string)
print(f"Number of unique characters: {unique_count}")
