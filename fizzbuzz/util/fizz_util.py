from fizzbuzz.globals import FIZZ_NUMBER
from fizzbuzz.util.number_util import NumberUtil


class FizzUtil(NumberUtil):
    def __init__(self):
        super().__init__(FIZZ_NUMBER)
