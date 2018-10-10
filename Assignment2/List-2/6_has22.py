def has22(nums):
  return 22 in [nums[i] * 10 + nums[i+1] for i in range(len(nums)-1)]
