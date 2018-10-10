def cat_dog(str):
  a = [str[i:i+3] for i in range(len(str)-2)]
  return a.count("cat") == a.count("dog")
