from fizzbuzz.util.fizz_buzz_string_builder import FizzBuzzStringBuilder
from fizzbuzz.util.fizz_buzz_util import FizzBuzzUtil
from fizzbuzz.util.number_util import NumberUtil


class FizzBuzzVerifier:
    def __init__(self):
        self.util = FizzBuzzUtil()

    def control(self, number):
        if self.util.is_fizzbuzz(number):
            return FizzBuzzStringBuilder.fizz() + FizzBuzzStringBuilder.buzz()
        elif self.util.is_fizz(number):
            return FizzBuzzStringBuilder.fizz()
        elif self.util.is_buzz(number):
            return FizzBuzzStringBuilder.buzz()
        else:
            return NumberUtil.to_string(number)
