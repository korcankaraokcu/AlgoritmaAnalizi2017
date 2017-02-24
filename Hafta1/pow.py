def recursive_pow(a,b):
  if b==0:
    return 1
  return a*recursive_pow(a,b-1)

print(recursive_pow(2,10))