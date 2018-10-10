def lucky_sum(a, b, c):
  nums = [a, b, c]
  for i in reversed(range(len(nums))):
    if nums[i] == 13:
      nums = nums[:i]
  return reduce(lambda x, y: x + y, nums, 0)
