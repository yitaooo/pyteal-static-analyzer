from antlr4 import *
from detectors.abstarct_detector import (
    AbstractDetector,
    DetectorClassification,
    DetectorType,
)
from detectors.utils import check_oncompletion


class UncheckedUpdatableApplication(AbstractDetector):  
    NAME = "unprotected-updatable"
    DESCRIPTION = "Unprotected Upgradable Applications"
    TYPE = DetectorType.STATEFUL
    IMPACT = DetectorClassification.HIGH

    update_app_checked = False
    
    update_app = "UpdateApplication"
    on_completion = "on_completion"

    def check_delete_appl(self, expr_ctx):
        return check_oncompletion(expr_ctx, self.update_app)

    def check_on_completion(self, expr_ctx):
        return check_oncompletion(expr_ctx, self.on_completion)

    def enterComparison(self, ctx):
        left_expr = ctx.expr(0)
        right_expr = ctx.expr(1)

        if self.check_on_completion(left_expr) and self.check_delete_appl(right_expr):
            self.update_app_checked= True


    def _check(self):
        return not self.update_app_checked
    