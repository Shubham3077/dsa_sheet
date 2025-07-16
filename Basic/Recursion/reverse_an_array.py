# Problem Statement: You are given an array. The task is to reverse the array and print it.

# Examples:

# Example 1:
# Input: N = 5, arr[] = {5, 4, 3, 2, 1}
# Output: {1, 2, 3, 4, 5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Example 2:
# Input: N = 6 arr[] = {10, 20, 30, 40}
# Output: {40, 30, 20, 10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# do this using recursion:

'''
approach: 1. starting from the first and last index of list, we want to reach till the half of the list.
so base condition will be if first index > lenght/2 return, and if not then exchange elms at first and last index
'''
def reverse_array(first, last, nums):
  if first > (len(nums) / 2):
    print(nums)
    return
  [nums[first], nums[last]] = [nums[last], nums[first]]

  reverse_array(first+1, last-1, nums)

list_nums = [1,2,3,4,5]
def main():
  reverse_array(0, len(list_nums)-1, list_nums)

main()
