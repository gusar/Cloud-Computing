oldnum = 0
num = 1

while len(str(num)) <= 1000:
  temp = num
  num += oldnum
  oldnum = temp

