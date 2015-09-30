# Python has the function for slicing strings. A string is first prepared
# by converting it to lower case to avoid errors.
# A string can then be sliced by each character in a reverse order and compared to the original.

# ask for input
s = str.lower(input("Enter a string: "))

# use slice function to reverse the string and check vs original
if s == s[::-1]:
# print result
  print(s, 'IS a palindrome')
else:
  print(s, 'is NOT a palidrome')