from fizzbuzz.util.buzz_util import BuzzUtil
from fizzbuzz.util.fizz_util import FizzUtil


class FizzBuzzUtil:
    def __init__(self):
        self.fizz_util = FizzUtil()
        self.buzz_util = BuzzUtil()

    def is_buzz(self, number):
        return self.buzz_util.is_dividable(number)

    def is_fizz(self, number):
        return self.fizz_util.is_dividable(number)

    def is_fizzbuzz(self, number):
        return self.is_fizz(number) and self.is_buzz(number)