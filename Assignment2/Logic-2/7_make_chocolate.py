def make_chocolate(small, big, goal):
  goal -= min(big, goal // 5) * 5
  if goal > small: return -1
  return goal
