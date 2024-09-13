def count_vowels(s):
    # Convert string to uppercase to handle both uppercase and lowercase uniformly
    s = s.upper()
    
    # Initialize a dictionary to hold the count of each vowel
    vowel_count = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    
    # Initialize total vowel count
    total_vowels = 0
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowel_count:
            vowel_count[char] += 1
            total_vowels += 1
    
    return total_vowels, vowel_count

# Given string
string = "Guvi Geeks Network Private Limited"

# Calculate vowel counts
total_vowels, vowel_count = count_vowels(string)

# Print the results
print(f"Total number of vowels: {total_vowels}")
print("Count of each vowel:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")

