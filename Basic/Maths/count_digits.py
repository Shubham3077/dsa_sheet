# Question: You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.

# Examples:
# Input: n = 4
# Output: 1
# Explanation: There is only 1 digit in 4.

# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

def count_digits(n):
  dig = 0
  while n > 0:
    n = n // 10
    dig += 1
  return dig

print(count_digits(40))
