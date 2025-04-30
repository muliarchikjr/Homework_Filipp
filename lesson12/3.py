
class Counter:

    def __init__(self, start_value=0):

        self.value = start_value
        self.start_value = start_value


    def increase(self, num=1):

        return self.value + num

    def decrease(self, num=1):

        return self.value - num

    def reset(self):

        return self.start_value

    