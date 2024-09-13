def are_anagrams(s1, s2):
    # Remove any whitespace and convert to lowercase for case-insensitive comparison
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(s1) != len(s2):
        return False
    
    # Create dictionaries to count the frequency of each character
    frequency1 = {}
    frequency2 = {}
    
    # Count frequencies in the first string
    for char in s1:
        frequency1[char] = frequency1.get(char, 0) + 1
    
    # Count frequencies in the second string
    for char in s2:
        frequency2[char] = frequency2.get(char, 0) + 1
    
    # Compare the frequency dictionaries
    return frequency1 == frequency2

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = are_anagrams(string1, string2)
print(f"Are the two strings anagrams? {result}")
