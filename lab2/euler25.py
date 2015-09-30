# Two number must be kept in memory: n-1 and n-2
# they are then used to calculate the next number.
# A count variable is used to keep track of the index.

oldnum = 0
num = 1
index = 0
#change num into string and check length
while len(str(num)) <= 1000:
  temp = num
  num += oldnum
  oldnum = temp
  index += 1
print(index)