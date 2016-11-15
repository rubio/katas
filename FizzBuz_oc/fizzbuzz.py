#! /usr/bin/env python

class FizzBuzz(object):

    def isFizz(self, x):
        return not (x % 3)

    def isBuzz(self, x):
        return not (x % 5)

    def say(self, x):
        if self.isFizz(x) and self.isBuzz(x):
            return 'FizzBuzz'
        elif self.isFizz(x):
            return 'Fizz'
        elif self.isBuzz(x):
            return 'Buzz'
        else:
            return x

fb = FizzBuzz()
for i in range(101):
    print fb.say(i)
