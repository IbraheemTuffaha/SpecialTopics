def string_splosion(str):
  return ''.join([str[:i] for i in range(len(str)+1)])
