#!/usr/bin/python
str = raw_input("Enter sequence of characters: ") #taking in word from command line

#print str #test to show the word
if str == str[::-1]:
   print str == str[::-1]
   print str[::-1]
else:
  print str[::-1]
  print("false")
