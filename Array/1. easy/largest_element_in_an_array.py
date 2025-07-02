# Ques: Given an array of integers nums, return the value of the largest element in the array

# Examples:
# Input: nums = [3, 3, 6, 1]

# Output: 6
# Explanation: The largest element in array is 6

# Input: nums = [3, 3, 0, 99, -40]

# Output: 99
# Explanation: The largest element in array is 99

'''
  Approach: 
  1. suppose 1st element in the array is maximum
  2. looping through the array, if current element > our element max becomes current element.
'''
def largest_num(nums):
  maxi = nums[0]

  for num in nums:
    if num > nums[0]:
      maxi = num

  return maxi


res = largest_num([3, 3, 6, 1])
print(res)
