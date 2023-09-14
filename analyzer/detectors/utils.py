from antlr4 import*
from pyteal.PyTealParser import PyTealParser

def check_oncompletion(expr_ctx, oncompletion_field):
        if expr_ctx is None:
            return False
        if isinstance(expr_ctx, TerminalNode):
            token = expr_ctx.symbol
            return token.text == oncompletion_field
        else:
            for child_ctx in expr_ctx.children:
                if check_oncompletion(child_ctx, oncompletion_field):
                    return True
            return False
        
def check_add_field(expr_ctx):
        if expr_ctx is None:
            return False
        if isinstance(expr_ctx, TerminalNode):
            token = expr_ctx.symbol
            return token.text == "Addr"
        else:
            for child_ctx in expr_ctx.children:
                if check_add_field(child_ctx):
                    return True
            return False
        
def check_gtxn(expr_ctx, txn_field):
        if expr_ctx is None:
            return False
        if isinstance(expr_ctx, TerminalNode):
            token = expr_ctx.symbol
            return token.text == txn_field
        else:
            for child_ctx in expr_ctx.children:
                if check_gtxn(child_ctx, txn_field):
                    return True
            return False
        
def check_expr(expr_ctx, expr_type):
        if expr_ctx is None:
            return False
        if not isinstance(expr_ctx, TerminalNode):
            if isinstance(expr_ctx, expr_type):
                return True
            else:
                for child_ctx in expr_ctx.children:  
                    if check_expr(child_ctx, expr_type):
                        return True
        return False

def check_intpay(expr_ctx):
        if expr_ctx is None:
            return False
        if not isinstance(expr_ctx, TerminalNode):
            if isinstance(expr_ctx, PyTealParser.Pyteal_integers_exprContext) and expr_ctx.getText() == "Int(1)":
                    return True
            else:
                for child_ctx in expr_ctx.children:  
                    if check_intpay(child_ctx):
                        return True

        return False

def check_intaxfer(expr_ctx):
        if expr_ctx is None:
            return False
        if not isinstance(expr_ctx, TerminalNode):
            if isinstance(expr_ctx, PyTealParser.Pyteal_integers_exprContext) and expr_ctx.getText() == "Int(4)":
                    return True
            else:
                for child_ctx in expr_ctx.children:  
                    if check_intaxfer(child_ctx):
                        return True

        return False