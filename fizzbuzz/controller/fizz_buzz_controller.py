from fizzbuzz.util.fizz_buzz_verifier import FizzBuzzVerifier
from fizzbuzz.util.number_util import NumberUtil


class FizzBuzzController:
    def __init__(self):
        self.verifier = FizzBuzzVerifier()
        self.result = []

    def run(self):
        while True:
            self.result = []
            input_str = input("Input your number: ")
            n = NumberUtil.to_number(input_str)

            for i in range(1, n + 1):
                item = self.control(i)
                self.append(item)

            print(self.result)

    def append(self, item):
        self.result.append(item)

    def control(self, number):
        return self.verifier.control(number)