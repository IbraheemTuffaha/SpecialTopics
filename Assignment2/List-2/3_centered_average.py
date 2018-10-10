def centered_average(nums):
  nums.sort()
  nums = nums[1: -1]
  return reduce(lambda x, y: x + y, nums) // len(nums)
