"""
  Recursion: when a function keeps calling itself, until a specified condition is met.
  some terms: stack overflow, segmentation error
"""
def main(): 
  f()
  return 0
count = 0
# this is a recursive function
def f():
  global count
  if count == 5: # base condition: to terminate the infinite recursive function
    return
  print(count)
  count += 1
  f()

main()

# basic recursion problems:
'''
-> print name 5 times ✅
-> print linearly from 1 to n ✅
-> print n to 1 ✅
-> print linearly from 1 to n but by backtracking ?
-> print from n to 1 but by backtracking 
'''

# here is no use of global variable, we are changing func parameters, also we are printing n to 1 here
def print_name(times, name):
  if times == 0:
    return
  print(times, name)
  print_name(times - 1, name)


def first_and_third():
  how_many_times = int(input("how many times do you want to print"))
  print_name(how_many_times, "Shubham")
  return 0

first_and_third()

def one_to_n(i, n):
  if i > n:
    return
  print(i)
  i += 1
  one_to_n(i, n)

def second():
  n = int(input())
  one_to_n(1, n)
  return 0

second()

# backtracking: as the name suggests, we track the function calls from last i.e after the base condition fulfills and returns the control to the previous func calls one by one, then they get executed...

# in this ex: print is after backtracking(recursive func), when i becomes 4, it returns the control, and 3,2,1 get printed
def backtracking(n, i):
  if i > n: 
    return
  
  backtracking(n, i+1) 
  print(i)

def fifth():
  n = int(input("to start backtracking from n to 1: ")) 
  backtracking(n, 1)
  return 0

fifth()

# dry run of above example: with recursion tree depiction of direction
"""
  n i   direction 
  3 1   ⬇️                                 ⬆️ 
  3 2   ⬇️                                 ⬆️ 
  3 3   ⬇️                                 ⬆️ 
  3 4   (base condition true so returns then direction become upwards)
"""
