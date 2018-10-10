def close_far(a, b, c):
  ab = abs(a-b)
  ac = abs(a-c)
  cb = abs(c - b)
  return cb >= 2 and (ab <= 1 and ac >= 2 or ac <= 1 and ab >= 2)
