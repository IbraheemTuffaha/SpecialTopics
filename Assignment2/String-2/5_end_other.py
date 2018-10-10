def end_other(a, b):
  l = min(len(a), len(b))
  return a.lower()[-l:] == b.lower()[-l:]
