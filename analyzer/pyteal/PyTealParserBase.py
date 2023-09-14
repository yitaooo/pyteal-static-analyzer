from antlr4 import *

class PyTealParserBase(Parser):

    def CannotBePlusMinus(self) -> bool:
        return True

    def CannotBeDotLpEq(self) -> bool:
        return True
