def count_hi(str):
  return [str[i:i+2] for i in range(len(str)-1)].count("hi")
