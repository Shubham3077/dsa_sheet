# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

# Examples:
# Input: N = 4
# Output: 10
# Explanation: first four natural numbers are 1, 2, 3, 4.
# Sum is 1 + 2 + 3 + 4 = > 10.

# Input: N = 2
# Output: 3
# Explanation: first two natural numbers are 1, 2.
# Sum is 1 + 2 = > 3.

"""
Approach: 1. we have to call recursive func 4 times. i is the iterable no from 1 -> n.
2. base condition should be if i > n: return
3. sum = sum + i. but for this sum should be global. ✅
4. (how would I do it with parameter only) -> pattern 2
5. (how would I do it with functions only) -> pattern 3
"""

total = 0
def sum_of_n_numbers(n, i):
  global total
  if i > n:
    return
  total = total + i
  sum_of_n_numbers(n, i+1)
  return total

# using parameter: using another func sum_using_parameters. THis is called parameterised recurison: here we can not return,
def sum_using_parameters(n, sum):
  if n < 1:
    print(sum)
    return

  sum_using_parameters(n-1, sum+n)

# functional recursion: to break larger problems into smaller ones to handle and return the answer
def functional_recursion(n):
  if n == 0:
    return 0

  return n + functional_recursion(n-1)

# task: factorial of n ex 4! = 24
def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)
# try to do this with parameterised recursion also 

def main():
  print(sum_of_n_numbers(4, 1))
  print(sum_using_parameters(4, 0), "why 0")
  print(functional_recursion(4), "functions are awesome")
  print(factorial(4))
  return 0

main()
