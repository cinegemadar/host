from waferslim.converters import convert_arg, convert_result, StrConverter
from ctypes import cdll

_STR_CONVERTER = StrConverter()

class Nav(object):
    def __init__(self):
        self._Source = 0
        self._Freq = 0
        self.lib = cdll.LoadLibrary('../lib/libnav.so')
        self.obj = self.lib.Nav_new()

    @convert_arg(to_type=int)
    def setSource(self, Source):
        ''' Sets a value - from a symbol that was created with echo '''
        self._Source = Source

    @convert_arg(to_type=int)
    def setFreq(self, Freq):
        ''' Sets a value - from a symbol that was created with echo '''
        self._Freq = Freq

    @convert_result(using=_STR_CONVERTER)
    def signal(self):
        return self.lib.Nav_getGPSSignal(self.obj, self._Source + self._Freq)

    def test(self):
        nav_lib.Nav_test(self.obj)

if __name__ == '__main__':
    nav = Nav()
    nav.setSource(10)
    nav.setFreq(20)
    print(nav.signal()) # expected 900
