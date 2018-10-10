def make_bricks(small, big, goal):
  return goal - min(big, goal // 5) * 5 <= small
