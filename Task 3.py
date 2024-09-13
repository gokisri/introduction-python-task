def remove_vowels(input_string):
    # Define the set of vowels (both uppercase and lowercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels
    filtered_characters = [char for char in input_string if char not in vowels]
    
    # Join the filtered characters into a new string
    result_string = ''.join(filtered_characters)
    
    return result_string

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("String without vowels:", remove_vowels(input_string))
