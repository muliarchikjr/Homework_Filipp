
class Counter:

    def __init__(self, value=0):

        self.value = value

    def increase(self, num=1):

        return self.value + num

    def decrease(self, num=1):

        return self.value - num

    def reset(self):

        return self.value

    