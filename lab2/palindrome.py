# ask for input
s = str.lower(input("Enter a string: "))

# use slice function to reverse the string and check vs original
if s == s[::-1]:
# print result
  print(s, ' IS a palindrome')
else:
  print(s, 'is NOT a palidrome')