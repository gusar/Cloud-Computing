# This version uses nested for loops to cycle through years, months, weeks and days.
# Each time year changes, leap year is determined. Then every week the number of
# the days are calculated which belong to the current month.
# A separate counter keeps track of the current day of the week.
# Every time if the week day counter index is zero, and the week index is zero,
# a sunday counter increments.

yearCount = 0
year = 1900
month = 0
week = 0
leap = False
dayrange = 6
sundayCount = 0
weekDay = 0

# count years
for year in range(1900, 2000):
  yearCount += 1
  # mark leap years
  if yearCount % 4 == 0 and year % 400 != 0:
    leap = True
  else:
    leap = False

  # count months
  for month in range (0, 12):

    # count weeks
    for week in range (0, 5):
      # last week of the month adjustment
      if week == 4:
        # 30-day months
        if month == 3 or month == 5 or month == 8 or month == 10:
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
      else:
        dayrange = 7

      # count days
      for day in range (0, dayrange):
        if weekDay > 7:
          weekDay = 0
        if week == 0 and weekDay == 0:
          sundayCount += 1
        weekDay += 1

# print result
print("\nSunday count in 18th century: ", sundayCount)

