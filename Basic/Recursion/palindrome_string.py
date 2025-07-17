# Question: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

# Examples:

# Example 1:
# Input: Str = “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.

'''
subproblems: 1. the string can contain characters.
2. can have upper and lowercase characters. -> so we have to remove whitespaces and characters and then join the string in lowercase
3. reverse the string and compare after reversing. if same palindrome else not

how to do it using recursion:

'''


def valid_palindrome(s, first, last):
  if first >= last:
    print("True")
    return True

  # if mismatch found, not a palindrome
  if s[first] != s[last]:
    print("False")
    return False
  
  valid_palindrome(s, first+1, last-1)

def main():
  s = input("Enter the string: ")
  cleaned_string = ''.join([char for char in s.lower() if char.isalnum()])
  valid_palindrome(cleaned_string, 0, len(cleaned_string)-1)

main()
