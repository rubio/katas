#! /usr/bin/env python

class BaseRule(object):
    def handles(self, x):
        pass

    def say(self, x):
        pass

class NormalRule(BaseRule):
    def handles(self, x):
        return True

    def say(self, x):
        return x

class FizzRule(BaseRule):
    def handles(self, x):
        return not x % 3

    def say(self, x):
        return 'Fizz'

class BuzzRule(BaseRule):
    def handles(self, x):
        return not x % 5

    def say(self, x):
        return 'Buzz'

class FizzBuzzRule(BaseRule):
    def handles(self, x):
        return not x % 3 and not x % 5

    def say(self, x):
        return 'FizzBuzz'

class WookRule(BaseRule):
    def handles(self, x):
        return not x % 7

    def say(self, x):
        return 'Wook'


class FizzBuzz(object):
    def __init__(self, rules):
        self.rules = rules

    def say(self, x):
        for r in self.rules:
            if r.handles(x):
                return r.say(x)


fb = FizzBuzz([FizzBuzzRule(), FizzRule(), BuzzRule(), WookRule(),  NormalRule()])
for i in range(11):
    print fb.say(i)
