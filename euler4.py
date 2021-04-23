# euler 4
# KeyJect
def isPal(num):
  ans = 0
  numSave = num
  while num>0:
    temp = num%10
    ans = ans*10 + temp
    num = int(num/10)
  if ans==numSave:
    return True
  return False

maxVar = 0
for i in range(1 , 1000):
  for j in range(1 , 1000):
    temp = i*j
    if isPal(temp):
      maxVar = max(maxVar , temp)
print(maxVar)