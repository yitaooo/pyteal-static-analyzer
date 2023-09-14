from antlr4 import *
from pyteal.PyTealParser import PyTealParser
from pyteal.PyTealParserListener import PyTealParserListener

class Mode(PyTealParserListener):
    def __init__(self):
        self.mode = None

    def check_mode(self, expr_ctx):
        if expr_ctx is None:
            return None 
        if not isinstance(expr_ctx, TerminalNode):
            if isinstance(expr_ctx, PyTealParser.Atom_exprContext):
                mode_text = expr_ctx.getText()
                if mode_text == "Mode.Signature":
                    return "Stateless"
                elif mode_text == "Mode.Application":
                    return "Stateful"
            else:

                for child_ctx in expr_ctx.children:
                    result = self.check_mode(child_ctx)
                    if result is not None:
                        return result  

        return None 

    def enterArgument(self, expr_ctx):
        mode = self.check_mode(expr_ctx) 
        if mode is not None:
            self.mode = mode
    
    def get_mode(self):
        return self.mode

