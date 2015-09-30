yearCount = 0
year = 1900
month = 0
week = 0
leap = false
for year in range(1900, 1999):
  count += 1
  if count % 4 == 0 and year % 400 != 0:
    leap true
  else
    leap false
  for month in range (0, 11):
    for week in range (0, 3):
      for day in range (0, 6):