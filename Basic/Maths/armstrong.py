# Question: You are given an integer n. You need to check whether it is an armstrong number or not . Return true if it is an armstrong number, otherwise return false.
# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Examples:
# Input: n = 153
# Output: true
# Explanation: Number of digits: 3.
# 13 + 53 + 33 = 1 + 125 + 27 = 153.

# Input: n = 12
# Output: false
# Explanation: Number of digits: 2.
# 12 + 22 = 1 + 4 = 5.

'''
approach: first we have to check how many digits
'''

def armstrong(num):
  x = num
  n = len(str(num))
  ans = 0
  while num != 0:
    dig = num % 10
    num = num // 10
    ans = ans + pow(dig, n)

  return True if x == ans else False

print(armstrong(12))
