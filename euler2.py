numsum = 0
oldnum = 0
num = 1
while num < 4000000:
  if num % 2 == 0:
    numsum += num
  temp = num
  num += oldnum
  oldnum = temp
print(numsum)