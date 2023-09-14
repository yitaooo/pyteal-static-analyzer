from antlr4 import *

from detectors.abstarct_detector import (
    AbstractDetector,
    DetectorClassification,
    DetectorType,
)
from detectors.utils import check_expr, check_add_field, check_intpay, check_gtxn



class CanCloseAccount(AbstractDetector):  
    NAME = "can-close-account"
    DESCRIPTION = "Missing CloseRemainderTo field Validation"
    TYPE = DetectorType.STATELESS
    IMPACT = DetectorClassification.HIGH

    account_checked = False
    is_payment = False

    def check_type(self, expr_ctx):
        return check_expr(expr_ctx, self.TYPEENUM) or check_gtxn(expr_ctx, "type_enum")
    
    def check_payment(self, expr_ctx):
        return check_expr(expr_ctx, self.PAYMENT)
    
    def check_payment_int(self, expr_ctx):
        return check_intpay(expr_ctx)

    def check_closeremainderto(self, expr_ctx):
        return check_expr(expr_ctx, self.CLOSEACCOUNT) or check_gtxn(expr_ctx, "close_remainder_to")

    def check_zeroaddr(self, expr_ctx):
        return check_expr(expr_ctx, self.ZEROADDR) 
    
    def check_addr(self, expr_ctx):
        return check_add_field(expr_ctx)
    

    def enterComparison(self, ctx):
        left_expr = ctx.expr(0)
        right_expr = ctx.expr(1)

        if self.check_type(left_expr):
            if self.check_payment(right_expr) or self.check_payment_int(right_expr):
                self.is_payment = True
        

        if self.check_closeremainderto(left_expr) and self.check_zeroaddr(right_expr) or self.check_addr(right_expr):
            self.account_checked = True


    def _check(self):
        #return True if transaction type is payment and CloseRemainder is not checked
        #return False if transaction type is not payment or CloseRemainder is checked
        return self.is_payment and not self.account_checked