def round10(num):
  mod = num % 10;
  return num - mod+ (mod >= 5) * 10 

def round_sum(a, b, c):
  return reduce(lambda x, y: x + y, list(map(round10, [a, b, c])))
