def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("True")
else:
    print("False")
