import calendar

sundayCount = 0
for year in range(1900, 2000):
  for month in range(1, 13):
    if calendar.weekday(year, month, 1) == 1:
      sundayCount += 1

print("The number of Sundays on the first day of the month in the 20th century is: ", sundayCount)