def longest_common_substring(s1, s2):
    # Initialize the length of the longest common substring
    m, n = len(s1), len(s2)
    # Create a 2D array to store lengths of longest common suffixes
    # dp[i][j] will be the length of longest common suffix of s1[0..i-1] and s2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the length and ending position of the longest common substring
    longest_length = 0
    end_pos_s1 = 0
    
    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    end_pos_s1 = i
            else:
                dp[i][j] = 0
    
    # Extract the longest common substring
    start_pos_s1 = end_pos_s1 - longest_length
    longest_common_substr = s1[start_pos_s1:end_pos_s1]
    
    return longest_common_substr

# Example usage
string1 = "abcdfghijk"
string2 = "abcfghijk"

result = longest_common_substring(string1, string2)
print("Longest common substring:", result)
