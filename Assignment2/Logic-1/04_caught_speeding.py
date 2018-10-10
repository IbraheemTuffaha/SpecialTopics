def caught_speeding(speed, is_birthday):
  if speed <= 60 + is_birthday * 5:
    return 0
  elif speed <= 80 + is_birthday * 5:
    return 1
  else:
    return 2
