def most_frequent_character(s):
    # Create a dictionary to store the frequency of each character
    frequency = {}
    
    # Loop through each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Find the character with the highest frequency
    most_frequent = None
    max_count = 0
    
    for char, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = char
    
    return most_frequent

# Example usage
input_string = input("Enter a string: ")
result = most_frequent_character(input_string)
print(f"The most frequent character is: '{result}'")
