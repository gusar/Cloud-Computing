oldnum = 0
num = 1
index = 0
while len(str(num)) <= 1000:
  temp = num
  num += oldnum
  oldnum = temp
  index += 1
print(index)