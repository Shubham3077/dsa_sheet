# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Examples:

# Example 1:
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6

# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

# can you do it without recursion, return a sequence
def fibo(n):
  nums = [0, 1]
  if n == 0:
    return 0
  for i in range(2, n+1):
    print(i)
    nums.append(nums[i-1]+nums[i-2])
  return nums

print(fibo(6)) 

# now with recursion: this is a classic case of multiple recursion with functional recursion
'''
approach: say f(5) = f(4) + f(3) ie f(n) = f(n-1) + f(n-2)
base condition: if n<=1: return n
IMP: if there exist multiple recursion call, it will execute one after another, later one will have to wait till the former one is completely executed.
'''
def func_recursion(n):
  if n <= 1:
    return n
  last = func_recursion(n-1)
  second_last = func_recursion(n-2)

  return last + second_last

def main():
  print(func_recursion(8))

main()
