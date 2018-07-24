from waferslim.converters import convert_arg, convert_result, StrConverter

_STR_CONVERTER = StrConverter()

class Calc(object):
    def __init__(self):
        self._A = 0
        self._B = 0

    @convert_arg(to_type=int)
    def setA(self, A):
        self._A = A

    @convert_arg(to_type=int)
    def setB(self, B):
        self._B = B

    @convert_result(using=_STR_CONVERTER)
    def multiply(self):
        return self._A * self._B

    def execute(self):
        pass

    def reset(self):
       pass

if __name__ == '__main__':
    c = Calc()
    c.setA(3)
    c.setB(4)
    print(c.multiply())
