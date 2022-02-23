class ICalc:
    def add(self, a, b):
        raise NotImplementedError

    def sub(self, a, b):
        raise NotImplementedError

    def mul(self, a, b):
        raise NotImplementedError

    def div(self, a, b):
        raise NotImplementedError


class Calc(ICalc):
    def add(self, a, b):
        return a + b


c = Calc()
print(c.add(3, 4))
