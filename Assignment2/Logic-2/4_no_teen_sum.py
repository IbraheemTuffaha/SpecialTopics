def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n

def no_teen_sum(a, b, c):
  return reduce(lambda x, y: x + y, list(map(fix_teen, [a, b, c])))
