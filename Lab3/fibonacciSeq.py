#!/usr/bin/python
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

counter = 0
value = 0

while(1000 != len(str(value))):
  counter = counter + 1
  value = fib(counter)

print ("Fib Seguence No:")
print value
print ("Fib Seguence Index:")
print counter

