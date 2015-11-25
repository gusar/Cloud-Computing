#!/usr/bin/python

totalDays = 0
startDate = 1901
endDate = 2001

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while(startDate != endDate):
  if startDate%4 == 0:
      months[1] = 29
  else:
    months[1] = 28
  for days in months:
    totalDays+=days
  startDate+=1

print totalDays
print totalDays / 7