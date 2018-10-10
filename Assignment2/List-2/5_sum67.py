def sum67(nums):
  ok, res= 1, 0
  for x in nums:
    if x == 6: ok = 0
    res += x * ok
    if x == 7: ok = 1
  return res
