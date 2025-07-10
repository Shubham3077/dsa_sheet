# Question: Given an integer array nums sorted in non-decreasing order, remove all duplicates in -place so that each unique element appears only once. Return the number of unique elements in the array.

# If the number of unique elements be k, then,
# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.
# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.

# Examples:
# Input: nums = [0, 0, 3, 3, 5, 6]
# Output: 4
# Explanation: Resulting array = [0, 3, 5, 6, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.

# Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]
# Output: 4
# Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.

'''
Approach:
1. starting with two pointers i, j. i = nums[0], j=i+1;
2. if both are equal pop j, j++ to check if next is also equal to i, else i++
3. return length of nums. 
'''

def removeDuplicates(nums):
  my_set = set()

  for i in range(len(nums)):
    my_set.add(nums[i])

  my_list = list(my_set)
  print(my_list)

  for i in range(len(my_list)):
    print(i, nums[i], my_list[i],"this seems fun isn't it" )
    nums[i] = my_list[i]
  
  return nums


res = removeDuplicates([-2, 2, 4, 4, 4, 4, 5, 5])
print(res)
