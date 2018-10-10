def array123(nums):
  return [1, 2, 3] in [nums[i:i+3] for i in range(len(nums) - 2)]
