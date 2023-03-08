def decode(data):
  result=""
  for c in data:
    result+=str((int(c)-3)%10)
  return result