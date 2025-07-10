# Question: You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

# Examples:
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.

def reverse_digits(n):
  rev_num = 0
  while n != 0:
    dig = n % 10
    n = n // 10
    rev_num = (rev_num*10) + dig
  
  return rev_num

res = reverse_digits(34)
print(res)

# but what about the -ve integer ? 
