# Question: You are given two integers n1 and n2. You need find the Greatest Common Divisor(GCD) of the two given numbers. Return the GCD of the two numbers.
# The Greatest Common Divisor(GCD) of two integers is the largest positive integer that divides both of the integers.

# Examples:
# Input: n1 = 4, n2 = 6
# Output: 2
# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
# Greatest Common divisor = 2.

# Input: n1 = 9, n2 = 8
# Output: 1
# Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
# Greatest Common divisor = 1.

'''
Approach: find from both number which is greater, 
starting from 2 run a for loop till that number, as 1 always divides all the numbers
'''

def gcd(num1, num2):
  highest = max(num1, num2)
  gcd = 1
  for num in range(2, highest+1, 1):
    if num1 % num == 0 and num2 % num == 0:
      gcd = num
  return gcd

print(gcd(15, 30))

