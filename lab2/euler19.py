yearCount = 0
year = 1900
month = 0
week = 0
leap = False
dayrange = 6
sundayCount = 0
weekDay = 0

# count years
for year in range(1900, 1999):
  yearCount += 1
  if yearCount % 4 == 0 and year % 400 != 0:
    leap = True
  else:
    leap = False

  # count months
  for month in range (0, 11):

    # count weeks
    for week in range (0, 4):
      if week == 4:
        if month == 3 or month == 5 or month == 8 or month == 11:
          dayrange = 2
        elif month == 1:
          if leap == False:
            dayrange = 0
          else:
            dayrange = 1
        else:
          dayrange = 3

      # count days
      for day in range (0, dayrange):
        if weekDay == 7:
          sundayCount += 1
          weekDay = 0
        else:
          weekDay += 1

# print result
print("\nSunday count in 18th century: ", sundayCount)

