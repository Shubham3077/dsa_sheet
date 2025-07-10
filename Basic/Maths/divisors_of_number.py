# Question: You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.

# Examples:
# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6.

# Input: n = 8
# Output: [1, 2, 4, 8]
# Explanation: The divisors of 8 are 1, 2, 4, 8.

def divisors(num):
  arr = []
  for i in range(1, num+1, 1):
    if num % i == 0:
      arr.append(i)

  return arr

res = divisors(9)
print(res)
