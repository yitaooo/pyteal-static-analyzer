from antlr4 import *
from detectors.abstarct_detector import (
    AbstractDetector,
    DetectorClassification,
    DetectorType,
)
from detectors.utils import check_expr, check_add_field, check_gtxn


class UncheckedRekeyto(AbstractDetector): 
    NAME = "rekey-to"
    DESCRIPTION = "Rekeyable Logic Signatures"
    TYPE = DetectorType.STATELESS
    IMPACT = DetectorClassification.HIGH

    rekeyto_validated = False
    asset_closed = False
    account_closed = False  

    def check_rekeyto(self, expr_ctx):
        #transaction field and group transaction check
        return check_expr(expr_ctx, self.REKEY) or check_gtxn(expr_ctx, "rekey_to")
    
    def check_assetcloseto(self, expr_ctx):
        return check_expr(expr_ctx, self.CLOSEASSET) or check_gtxn(expr_ctx, "asset_close_to")

    def check_closeremainderto(self, expr_ctx):
        return check_expr(expr_ctx, self.CLOSEACCOUNT) or check_gtxn(expr_ctx, "close_remainder_to")

    def check_zeroaddr(self, expr_ctx):
        return check_expr(expr_ctx, self.ZEROADDR) 
    
    def check_addr(self, expr_ctx):
        return check_add_field(expr_ctx)

    def enterComparison(self, ctx):
        left_expr = ctx.expr(0)
        right_expr = ctx.expr(1)

        if self.check_rekeyto(left_expr) and (self.check_zeroaddr(right_expr) or self.check_addr(right_expr)):
            self.rekeyto_validated = True
        
        if self.check_assetcloseto(left_expr):
            if self.check_zeroaddr(right_expr):
                self.asset_closed = False
            elif self.check_addr(right_expr):
                self.asset_closed = True

        if self.check_closeremainderto(left_expr):
            if self.check_zeroaddr(right_expr):
                self.account_closed = False
            elif self.check_addr(right_expr):
                self.account_closed = True
        
    def _check(self):
        return not self.rekeyto_validated and (not self.asset_closed or not self.account_closed)
        

    
