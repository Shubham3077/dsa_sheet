# Question: You are given an integer n. You need to check whether the number is a palindrome number or not . Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.


# Examples:
# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.

# Input: n = 123
# Output: false
# Explanation: When read from left to right : 123.

'''
Approach: 
'''

def check_palindrome(n):
  rev_num = 0
  num = n
  while n != 0:
    dig = n % 10
    n = n // 10
    rev_num = (rev_num*10) + dig

  return True if num == rev_num else False

print(check_palindrome(125))
