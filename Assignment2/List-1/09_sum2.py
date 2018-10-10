def sum2(nums):
  return reduce(lambda x, y: x + y, nums[:2], 0)
