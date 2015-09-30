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
  # mark leap years
  if yearCount % 4 == 0 and year % 400 != 0:
    leap = True
  else:
    leap = False

  # count months
  for month in range (0, 11):

    # count weeks
    for week in range (0, 4):
      # last week of the month adjustment
      if week == 4:
        # 30-day months
        if month == 3 or month == 5 or month == 8 or month == 11:
          dayrange = 2
        # february case
        elif month == 1:
          if leap == False:
            dayrange = 0
          else:
            dayrange = 1
        # 31-day months
        else:
          dayrange = 3

      # count days
      for day in range (0, dayrange):
        # reset week each 7 days
        if weekDay == 7:
          sundayCount += 1
          weekDay = 0
        else:
          weekDay += 1

# print result
print("\nSunday count in 18th century: ", sundayCount)

