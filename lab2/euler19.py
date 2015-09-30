yearCount = 0
year = 1900
month = 0
week = 0
leap = false
dayrange = 6
sundayCount = 0
weekDay = 0

for year in range(1900, 1999):
  count += 1
  if count % 4 == 0 and year % 400 != 0:
    leap true
  else
    leap false
  for month in range (0, 11):
    for week in range (0, 4):
      if week == 4:
        if month == 3 or month == 5 or month == 8 or month == 11:
          dayrange = 2
        else if month == 1:
          if leap == false:
            dayrange = 0
          else:
            dayrange = 1
        else:
          dayrange = 3
      for day in range (0, dayrange):
        if weekDay == 7:
          sundayCount += 1
          weekDay = 0
        weekDay +1

print(sundayCount)

