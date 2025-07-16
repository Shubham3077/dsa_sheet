# Problem Statement: Given a number X, print its factorial.

# To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

# Note: X is always a positive number.

# -> done using parameterised way of recursion
def factorial(n, fact):
  if n == 1:
    print(fact)
    return
  
  factorial(n-1, fact*n)

def main():
  factorial(6, 1)

main()
