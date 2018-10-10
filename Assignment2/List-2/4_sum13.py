def sum13(nums):
  for i in reversed(range(len(nums))):
    if nums[i] == 13:
      nums = nums[:i] + nums[i+2:]
  return reduce(lambda x, y: x + y, nums, 0)
