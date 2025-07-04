# Ques: Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

# Examples:
# Input: nums = [1, 2, 3, 4, 5]
# Output: true
# Explanation: For all i(1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

# Input: nums = [1, 2, 1, 4, 5]
# Output: false
# Explanation: For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

'''
Approach: 
1. loop through the list staring from the 1st elm
2. if all elm >= then the previous elms, then list is sorted else not sorted
3. also if not (nums[i] >= nums[0] and nums[i] <= nums[i+1]): this is unneccesary checking but logic here is also correct.
'''

def isSorted(nums):
  res = True
  for i in range(1, len(nums), 1):
    print(nums[i], nums[i-1])
    if nums[i] >= nums[i-1]:
      res = True
    else: 
      res = False # jaise hi ek br bhi false, aae break loop and return false(the list is not sorted)
      break
  return res


res = isSorted([1, 2, 3, 4, 4, 5, 7])
print(res, "result")
