from fizzbuzz.globals import BUZZ_NUMBER
from fizzbuzz.util.number_util import NumberUtil


class BuzzUtil(NumberUtil):
    def __init__(self):
        super().__init__(BUZZ_NUMBER)