def count_code(str):
  a = [str[i:i+2] + 'd' + str[i+3] for i in range(len(str)-3)]
  return a.count("code")
