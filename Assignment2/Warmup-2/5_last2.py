def last2(str):
  return [str[i:i+2] for i in range(len(str)-1)].count(str[-2:]) - (len(str[-2:]) == 2)
