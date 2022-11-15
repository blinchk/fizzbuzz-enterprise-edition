class NumberUtil:
    def __init__(self, number):
        self.number = number

    def is_dividable(self, n):
        return n % self.number == 0

    @staticmethod
    def to_number(str):
        try:
            return int(str)
        except:
            raise ValueError("This is not integer, sorry")

    @staticmethod
    def to_string(number):
        return str(number)