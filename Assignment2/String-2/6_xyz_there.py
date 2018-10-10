def xyz_there(str):
  a = [str[i:i+3] for i in range(len(str)-2) if i == 0 or str[i-1] != '.']
  return "xyz" in a
