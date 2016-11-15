#! /usr/bin/env python

for i in range(101):
    is3 = not(i % 3)
    is5 = not(i % 5)
    if is3 and is5:
        print 'FizzBuzz'
        continue
    if is3:
        print 'Fizz'
        continue
    if is5:
        print 'Buzz'
        continue
    print i
