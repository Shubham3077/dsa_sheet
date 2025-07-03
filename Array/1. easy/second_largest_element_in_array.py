# Ques: Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

# Examples:
# Input: nums = [8, 8, 7, 6, 5]
# Output: 7
# Explanation: The largest value in nums is 8, the second largest is 7

# Input: nums = [10, 10, 10, 10, 10]
# Output: -1
# Explanation: The only value in nums is 10, so there is no second largest value, thus - 1 is returned

'''
  Approach:
  (Brute force approach)
  1. sort the list, and find the maximum number already.
  2. loop from end to start, if the prev element < max, it is second largest, and break.
  3. no second largest, then -1.

  (Better approach)
  find the largest element, then again loop through list & check if current elm > second(init with -1) and != largest then it's second largest.

  (optimal approach)
  1. let first elm is largest, let second largest is smallest -ve int. 
  2. loop through the list, if next elm > largest, its largest and second largest becomes the previous largest elm
  3. Note: if next elm <= largest, not do anything. 
  
'''

def second_largest(nums):
  maxi = max(nums)
  second = -1
  nums.sort()
  for i in range(len(nums)-1, -1, -1):
    if nums[i] < maxi:
      second = nums[i]
      break

  return second 

res = second_largest([4, 5])
print(res, "the final answer")

def better_approach(nums):
  # find largest element first
  largest = nums[0]
  second = -1
  for num in range(len(nums)-1):
    if num > largest:
      largest = num

  for i in range(0, len(nums)-1, 1 ):
    if nums[i] > second and nums[i] != largest:
      second = nums[i]
  
  return second

res2 = better_approach([10,10])
print(res2, 'is the final answer')


def most_optimal(nums):
  largest = nums[0]
  second = -1 # if there is no -ve int in list
  for i in range(1, len(nums), 1):
    print(second, largest, i)
    if nums[i] > largest :
      second = largest
      largest = nums[i]
    elif nums[i] < largest and nums[i] > second:
      second = nums[i]

  return second


res3 = most_optimal([8, 8, 7, 6, 5])
print(res3, "is most optimal")
