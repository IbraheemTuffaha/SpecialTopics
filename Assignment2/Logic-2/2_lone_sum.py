def lone_sum(a, b, c):
  nums = [a, b, c]
  return reduce(lambda x, y: x + y, [x for x in nums if nums.count(x) == 1], 0)
