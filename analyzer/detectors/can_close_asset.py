from antlr4 import *


from detectors.utils import check_expr, check_add_field, check_intaxfer, check_gtxn
from detectors.abstarct_detector import (
    AbstractDetector,
    DetectorClassification,
    DetectorType,
)


class CanCloseAsset(AbstractDetector):  
    NAME = "can-close-asset"
    DESCRIPTION = "Missing AssetCloseTo Field Validation"
    TYPE = DetectorType.STATELESS
    IMPACT = DetectorClassification.HIGH

    is_axfer = False
    asset_checked = False


    def check_type(self, expr_ctx):
        return check_expr(expr_ctx, self.TYPEENUM) or check_gtxn(expr_ctx, "type_enum")
    
    def check_axfer(self, expr_ctx):
        return check_expr(expr_ctx, self.AXFER)
    
    def check_axfer_int(self, expr_ctx):
        return check_intaxfer(expr_ctx)

    def check_assetcloseto(self, expr_ctx):
        return check_expr(expr_ctx, self.CLOSEASSET) or check_gtxn(expr_ctx, "asset_close_to")

    def check_zeroaddr(self, expr_ctx):
        return check_expr(expr_ctx, self.ZEROADDR)
    
    def check_addr(self, expr_ctx):
        return check_add_field(expr_ctx)

    def enterComparison(self, ctx):
        left_expr = ctx.expr(0)
        right_expr = ctx.expr(1)

        if self.check_type(left_expr):
            if self.check_axfer(right_expr) or self.check_axfer_int(right_expr):
                self.is_axfer = True

        if self.check_assetcloseto(left_expr):
            if self.check_zeroaddr(right_expr) or self.check_addr(right_expr):
                self.asset_checked = True


    def _check(self):
        #return True if transaction type is Axfer and AssetClose is not checked
        #return False if transaction type is not Axfer or AssetClose is checked
        return self.is_axfer and not self.asset_checked
    