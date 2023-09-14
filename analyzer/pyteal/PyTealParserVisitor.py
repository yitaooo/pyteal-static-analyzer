# Generated from PyTealParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PyTealParser import PyTealParser
else:
    from PyTealParser import PyTealParser

# This class defines a complete generic visitor for a parse tree produced by PyTealParser.

class PyTealParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PyTealParser#file_input.
    def visitFile_input(self, ctx:PyTealParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#single_input.
    def visitSingle_input(self, ctx:PyTealParser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#eval_input.
    def visitEval_input(self, ctx:PyTealParser.Eval_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#decorator.
    def visitDecorator(self, ctx:PyTealParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#decorators.
    def visitDecorators(self, ctx:PyTealParser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#decorated.
    def visitDecorated(self, ctx:PyTealParser.DecoratedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#async_funcdef.
    def visitAsync_funcdef(self, ctx:PyTealParser.Async_funcdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#funcdef.
    def visitFuncdef(self, ctx:PyTealParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#parameters.
    def visitParameters(self, ctx:PyTealParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#typedargslist.
    def visitTypedargslist(self, ctx:PyTealParser.TypedargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#tfpdef.
    def visitTfpdef(self, ctx:PyTealParser.TfpdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#varargslist.
    def visitVarargslist(self, ctx:PyTealParser.VarargslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#vfpdef.
    def visitVfpdef(self, ctx:PyTealParser.VfpdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#stmt.
    def visitStmt(self, ctx:PyTealParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#simple_stmts.
    def visitSimple_stmts(self, ctx:PyTealParser.Simple_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#simple_stmt.
    def visitSimple_stmt(self, ctx:PyTealParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#expr_stmt.
    def visitExpr_stmt(self, ctx:PyTealParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#annassign.
    def visitAnnassign(self, ctx:PyTealParser.AnnassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#testlist_star_expr.
    def visitTestlist_star_expr(self, ctx:PyTealParser.Testlist_star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#augassign.
    def visitAugassign(self, ctx:PyTealParser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#del_stmt.
    def visitDel_stmt(self, ctx:PyTealParser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pass_stmt.
    def visitPass_stmt(self, ctx:PyTealParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#flow_stmt.
    def visitFlow_stmt(self, ctx:PyTealParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#break_stmt.
    def visitBreak_stmt(self, ctx:PyTealParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#continue_stmt.
    def visitContinue_stmt(self, ctx:PyTealParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#return_stmt.
    def visitReturn_stmt(self, ctx:PyTealParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#yield_stmt.
    def visitYield_stmt(self, ctx:PyTealParser.Yield_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#raise_stmt.
    def visitRaise_stmt(self, ctx:PyTealParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#import_stmt.
    def visitImport_stmt(self, ctx:PyTealParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#import_name.
    def visitImport_name(self, ctx:PyTealParser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#import_from.
    def visitImport_from(self, ctx:PyTealParser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#import_as_name.
    def visitImport_as_name(self, ctx:PyTealParser.Import_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#dotted_as_name.
    def visitDotted_as_name(self, ctx:PyTealParser.Dotted_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#import_as_names.
    def visitImport_as_names(self, ctx:PyTealParser.Import_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#dotted_as_names.
    def visitDotted_as_names(self, ctx:PyTealParser.Dotted_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#dotted_name.
    def visitDotted_name(self, ctx:PyTealParser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#global_stmt.
    def visitGlobal_stmt(self, ctx:PyTealParser.Global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx:PyTealParser.Nonlocal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#assert_stmt.
    def visitAssert_stmt(self, ctx:PyTealParser.Assert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#compound_stmt.
    def visitCompound_stmt(self, ctx:PyTealParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#async_stmt.
    def visitAsync_stmt(self, ctx:PyTealParser.Async_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#if_stmt.
    def visitIf_stmt(self, ctx:PyTealParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#while_stmt.
    def visitWhile_stmt(self, ctx:PyTealParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#for_stmt.
    def visitFor_stmt(self, ctx:PyTealParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#try_stmt.
    def visitTry_stmt(self, ctx:PyTealParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#with_stmt.
    def visitWith_stmt(self, ctx:PyTealParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#with_item.
    def visitWith_item(self, ctx:PyTealParser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#except_clause.
    def visitExcept_clause(self, ctx:PyTealParser.Except_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#block.
    def visitBlock(self, ctx:PyTealParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#match_stmt.
    def visitMatch_stmt(self, ctx:PyTealParser.Match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#subject_expr.
    def visitSubject_expr(self, ctx:PyTealParser.Subject_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#star_named_expressions.
    def visitStar_named_expressions(self, ctx:PyTealParser.Star_named_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#star_named_expression.
    def visitStar_named_expression(self, ctx:PyTealParser.Star_named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#case_block.
    def visitCase_block(self, ctx:PyTealParser.Case_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#guard.
    def visitGuard(self, ctx:PyTealParser.GuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#patterns.
    def visitPatterns(self, ctx:PyTealParser.PatternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pattern.
    def visitPattern(self, ctx:PyTealParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#as_pattern.
    def visitAs_pattern(self, ctx:PyTealParser.As_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#or_pattern.
    def visitOr_pattern(self, ctx:PyTealParser.Or_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#closed_pattern.
    def visitClosed_pattern(self, ctx:PyTealParser.Closed_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#literal_pattern.
    def visitLiteral_pattern(self, ctx:PyTealParser.Literal_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#literal_expr.
    def visitLiteral_expr(self, ctx:PyTealParser.Literal_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#complex_number.
    def visitComplex_number(self, ctx:PyTealParser.Complex_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#signed_number.
    def visitSigned_number(self, ctx:PyTealParser.Signed_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#signed_real_number.
    def visitSigned_real_number(self, ctx:PyTealParser.Signed_real_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#real_number.
    def visitReal_number(self, ctx:PyTealParser.Real_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#imaginary_number.
    def visitImaginary_number(self, ctx:PyTealParser.Imaginary_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#capture_pattern.
    def visitCapture_pattern(self, ctx:PyTealParser.Capture_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pattern_capture_target.
    def visitPattern_capture_target(self, ctx:PyTealParser.Pattern_capture_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#wildcard_pattern.
    def visitWildcard_pattern(self, ctx:PyTealParser.Wildcard_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#value_pattern.
    def visitValue_pattern(self, ctx:PyTealParser.Value_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#attr.
    def visitAttr(self, ctx:PyTealParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#name_or_attr.
    def visitName_or_attr(self, ctx:PyTealParser.Name_or_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#group_pattern.
    def visitGroup_pattern(self, ctx:PyTealParser.Group_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#sequence_pattern.
    def visitSequence_pattern(self, ctx:PyTealParser.Sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#open_sequence_pattern.
    def visitOpen_sequence_pattern(self, ctx:PyTealParser.Open_sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#maybe_sequence_pattern.
    def visitMaybe_sequence_pattern(self, ctx:PyTealParser.Maybe_sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#maybe_star_pattern.
    def visitMaybe_star_pattern(self, ctx:PyTealParser.Maybe_star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#star_pattern.
    def visitStar_pattern(self, ctx:PyTealParser.Star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#mapping_pattern.
    def visitMapping_pattern(self, ctx:PyTealParser.Mapping_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#items_pattern.
    def visitItems_pattern(self, ctx:PyTealParser.Items_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#key_value_pattern.
    def visitKey_value_pattern(self, ctx:PyTealParser.Key_value_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#double_star_pattern.
    def visitDouble_star_pattern(self, ctx:PyTealParser.Double_star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#class_pattern.
    def visitClass_pattern(self, ctx:PyTealParser.Class_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#positional_patterns.
    def visitPositional_patterns(self, ctx:PyTealParser.Positional_patternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#keyword_patterns.
    def visitKeyword_patterns(self, ctx:PyTealParser.Keyword_patternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#keyword_pattern.
    def visitKeyword_pattern(self, ctx:PyTealParser.Keyword_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#test.
    def visitTest(self, ctx:PyTealParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#test_nocond.
    def visitTest_nocond(self, ctx:PyTealParser.Test_nocondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#lambdef.
    def visitLambdef(self, ctx:PyTealParser.LambdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#lambdef_nocond.
    def visitLambdef_nocond(self, ctx:PyTealParser.Lambdef_nocondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#or_test.
    def visitOr_test(self, ctx:PyTealParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#and_test.
    def visitAnd_test(self, ctx:PyTealParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#not_test.
    def visitNot_test(self, ctx:PyTealParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#comparison.
    def visitComparison(self, ctx:PyTealParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#comp_op.
    def visitComp_op(self, ctx:PyTealParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#star_expr.
    def visitStar_expr(self, ctx:PyTealParser.Star_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#expr.
    def visitExpr(self, ctx:PyTealParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_data_expr.
    def visitPyteal_data_expr(self, ctx:PyTealParser.Pyteal_data_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_integers_expr.
    def visitPyteal_integers_expr(self, ctx:PyTealParser.Pyteal_integers_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_expr.
    def visitPyteal_bytes_expr(self, ctx:PyTealParser.Pyteal_bytes_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_base.
    def visitPyteal_bytes_base(self, ctx:PyTealParser.Pyteal_bytes_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_conversion_expr.
    def visitPyteal_conversion_expr(self, ctx:PyTealParser.Pyteal_conversion_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_arithmetic_operations.
    def visitPyteal_arithmetic_operations(self, ctx:PyTealParser.Pyteal_arithmetic_operationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_comparison.
    def visitPyteal_comparison(self, ctx:PyTealParser.Pyteal_comparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_comp_op.
    def visitPyteal_comp_op(self, ctx:PyTealParser.Pyteal_comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_comparison.
    def visitPyteal_bytes_comparison(self, ctx:PyTealParser.Pyteal_bytes_comparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_comp_op.
    def visitPyteal_bytes_comp_op(self, ctx:PyTealParser.Pyteal_bytes_comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_or_expr.
    def visitPyteal_or_expr(self, ctx:PyTealParser.Pyteal_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_and_expr.
    def visitPyteal_and_expr(self, ctx:PyTealParser.Pyteal_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_not_expr.
    def visitPyteal_not_expr(self, ctx:PyTealParser.Pyteal_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_exp_expr.
    def visitPyteal_exp_expr(self, ctx:PyTealParser.Pyteal_exp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_add_expr.
    def visitPyteal_add_expr(self, ctx:PyTealParser.Pyteal_add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_minus_expr.
    def visitPyteal_minus_expr(self, ctx:PyTealParser.Pyteal_minus_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bitwise_not_expr.
    def visitPyteal_bitwise_not_expr(self, ctx:PyTealParser.Pyteal_bitwise_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_mul_expr.
    def visitPyteal_mul_expr(self, ctx:PyTealParser.Pyteal_mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_div_expr.
    def visitPyteal_div_expr(self, ctx:PyTealParser.Pyteal_div_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_mod_expr.
    def visitPyteal_mod_expr(self, ctx:PyTealParser.Pyteal_mod_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bitwise_and_expr.
    def visitPyteal_bitwise_and_expr(self, ctx:PyTealParser.Pyteal_bitwise_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bitwise_xor_expr.
    def visitPyteal_bitwise_xor_expr(self, ctx:PyTealParser.Pyteal_bitwise_xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bitwise_or_expr.
    def visitPyteal_bitwise_or_expr(self, ctx:PyTealParser.Pyteal_bitwise_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_or_expr.
    def visitPyteal_bytes_or_expr(self, ctx:PyTealParser.Pyteal_bytes_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_and_expr.
    def visitPyteal_bytes_and_expr(self, ctx:PyTealParser.Pyteal_bytes_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_not_expr.
    def visitPyteal_bytes_not_expr(self, ctx:PyTealParser.Pyteal_bytes_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_mul_expr.
    def visitPyteal_bytes_mul_expr(self, ctx:PyTealParser.Pyteal_bytes_mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_div_expr.
    def visitPyteal_bytes_div_expr(self, ctx:PyTealParser.Pyteal_bytes_div_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_mod_expr.
    def visitPyteal_bytes_mod_expr(self, ctx:PyTealParser.Pyteal_bytes_mod_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_add_expr.
    def visitPyteal_bytes_add_expr(self, ctx:PyTealParser.Pyteal_bytes_add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_minus_expr.
    def visitPyteal_bytes_minus_expr(self, ctx:PyTealParser.Pyteal_bytes_minus_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_xor_expr.
    def visitPyteal_bytes_xor_expr(self, ctx:PyTealParser.Pyteal_bytes_xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_bytes_zero_expr.
    def visitPyteal_bytes_zero_expr(self, ctx:PyTealParser.Pyteal_bytes_zero_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_expr.
    def visitPyteal_txn_expr(self, ctx:PyTealParser.Pyteal_txn_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_type_expr.
    def visitPyteal_txn_type_expr(self, ctx:PyTealParser.Pyteal_txn_type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_type_enum_expr.
    def visitPyteal_txn_type_enum_expr(self, ctx:PyTealParser.Pyteal_txn_type_enum_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_sender_expr.
    def visitPyteal_txn_sender_expr(self, ctx:PyTealParser.Pyteal_txn_sender_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_fee_expr.
    def visitPyteal_txn_fee_expr(self, ctx:PyTealParser.Pyteal_txn_fee_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_first_valid_expr.
    def visitPyteal_txn_first_valid_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_first_valid_time_expr.
    def visitPyteal_txn_first_valid_time_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_time_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_last_valid_expr.
    def visitPyteal_txn_last_valid_expr(self, ctx:PyTealParser.Pyteal_txn_last_valid_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_note_expr.
    def visitPyteal_txn_note_expr(self, ctx:PyTealParser.Pyteal_txn_note_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_lease_expr.
    def visitPyteal_txn_lease_expr(self, ctx:PyTealParser.Pyteal_txn_lease_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_group_index_expr.
    def visitPyteal_txn_group_index_expr(self, ctx:PyTealParser.Pyteal_txn_group_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_tx_id_expr.
    def visitPyteal_txn_tx_id_expr(self, ctx:PyTealParser.Pyteal_txn_tx_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_rekey_to_expr.
    def visitPyteal_txn_rekey_to_expr(self, ctx:PyTealParser.Pyteal_txn_rekey_to_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_application_id_expr.
    def visitPyteal_txn_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_application_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_on_completion_expr.
    def visitPyteal_txn_on_completion_expr(self, ctx:PyTealParser.Pyteal_txn_on_completion_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_approval_program_expr.
    def visitPyteal_txn_approval_program_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_global_num_uints_expr.
    def visitPyteal_txn_global_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_uints_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_global_num_byte_slices_expr.
    def visitPyteal_txn_global_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_byte_slices_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_local_num_uints_expr.
    def visitPyteal_txn_local_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_uints_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_local_num_byte_slices_expr.
    def visitPyteal_txn_local_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_byte_slices_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_accounts_expr.
    def visitPyteal_txn_accounts_expr(self, ctx:PyTealParser.Pyteal_txn_accounts_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_assets_expr.
    def visitPyteal_txn_assets_expr(self, ctx:PyTealParser.Pyteal_txn_assets_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_applications_expr.
    def visitPyteal_txn_applications_expr(self, ctx:PyTealParser.Pyteal_txn_applications_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_expr.
    def visitPyteal_txn_clear_state_program_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_extra_program_pages_expr.
    def visitPyteal_txn_extra_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_extra_program_pages_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_application_args_expr.
    def visitPyteal_txn_application_args_expr(self, ctx:PyTealParser.Pyteal_txn_application_args_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_created_application_id_expr.
    def visitPyteal_txn_created_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_application_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_logs_expr.
    def visitPyteal_txn_logs_expr(self, ctx:PyTealParser.Pyteal_txn_logs_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_last_log_expr.
    def visitPyteal_txn_last_log_expr(self, ctx:PyTealParser.Pyteal_txn_last_log_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_approval_program_pages_expr.
    def visitPyteal_txn_approval_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_pages_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_pages_expr.
    def visitPyteal_txn_clear_state_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_pages_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_expr.
    def visitPyteal_txn_config_asset_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_total_expr.
    def visitPyteal_txn_config_asset_total_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_total_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_decimals_expr.
    def visitPyteal_txn_config_asset_decimals_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_decimals_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_default_frozen_expr.
    def visitPyteal_txn_config_asset_default_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_default_frozen_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_unit_name_expr.
    def visitPyteal_txn_config_asset_unit_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_unit_name_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_name_expr.
    def visitPyteal_txn_config_asset_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_name_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_url_expr.
    def visitPyteal_txn_config_asset_url_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_url_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_metadata_hash_expr.
    def visitPyteal_txn_config_asset_metadata_hash_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_metadata_hash_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_manager_expr.
    def visitPyteal_txn_config_asset_manager_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_manager_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_reserve_expr.
    def visitPyteal_txn_config_asset_reserve_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_reserve_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_freeze_expr.
    def visitPyteal_txn_config_asset_freeze_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_freeze_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_config_asset_clawback_expr.
    def visitPyteal_txn_config_asset_clawback_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_clawback_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_created_asset_id_expr.
    def visitPyteal_txn_created_asset_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_asset_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_expr.
    def visitPyteal_txn_freeze_asset_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_account_expr.
    def visitPyteal_txn_freeze_asset_account_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_account_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_frozen_expr.
    def visitPyteal_txn_freeze_asset_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_frozen_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_xfer_asset_expr.
    def visitPyteal_txn_xfer_asset_expr(self, ctx:PyTealParser.Pyteal_txn_xfer_asset_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_asset_amount_expr.
    def visitPyteal_txn_asset_amount_expr(self, ctx:PyTealParser.Pyteal_txn_asset_amount_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_asset_sender_expr.
    def visitPyteal_txn_asset_sender_expr(self, ctx:PyTealParser.Pyteal_txn_asset_sender_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_asset_receiver_expr.
    def visitPyteal_txn_asset_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_asset_receiver_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_asset_close_to_expr.
    def visitPyteal_txn_asset_close_to_expr(self, ctx:PyTealParser.Pyteal_txn_asset_close_to_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_vote_pk_expr.
    def visitPyteal_txn_vote_pk_expr(self, ctx:PyTealParser.Pyteal_txn_vote_pk_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_selection_pk_expr.
    def visitPyteal_txn_selection_pk_expr(self, ctx:PyTealParser.Pyteal_txn_selection_pk_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_state_proof_pk_expr.
    def visitPyteal_txn_state_proof_pk_expr(self, ctx:PyTealParser.Pyteal_txn_state_proof_pk_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_vote_first_expr.
    def visitPyteal_txn_vote_first_expr(self, ctx:PyTealParser.Pyteal_txn_vote_first_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_vote_last_expr.
    def visitPyteal_txn_vote_last_expr(self, ctx:PyTealParser.Pyteal_txn_vote_last_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_vote_key_dilution_expr.
    def visitPyteal_txn_vote_key_dilution_expr(self, ctx:PyTealParser.Pyteal_txn_vote_key_dilution_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_nonparticipation_expr.
    def visitPyteal_txn_nonparticipation_expr(self, ctx:PyTealParser.Pyteal_txn_nonparticipation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_receiver_expr.
    def visitPyteal_txn_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_receiver_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_amount_expr.
    def visitPyteal_txn_amount_expr(self, ctx:PyTealParser.Pyteal_txn_amount_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txn_close_remainder_to_expr.
    def visitPyteal_txn_close_remainder_to_expr(self, ctx:PyTealParser.Pyteal_txn_close_remainder_to_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_Unknown_expr.
    def visitPyteal_txntype_Unknown_expr(self, ctx:PyTealParser.Pyteal_txntype_Unknown_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_Payment_expr.
    def visitPyteal_txntype_Payment_expr(self, ctx:PyTealParser.Pyteal_txntype_Payment_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_KeyRegistration_expr.
    def visitPyteal_txntype_KeyRegistration_expr(self, ctx:PyTealParser.Pyteal_txntype_KeyRegistration_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_AssetConfig_expr.
    def visitPyteal_txntype_AssetConfig_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetConfig_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_AssetTransfer_expr.
    def visitPyteal_txntype_AssetTransfer_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetTransfer_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_AssetFreeze_expr.
    def visitPyteal_txntype_AssetFreeze_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetFreeze_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_txntype_ApplicationCall_expr.
    def visitPyteal_txntype_ApplicationCall_expr(self, ctx:PyTealParser.Pyteal_txntype_ApplicationCall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_min_txn_fee_expr.
    def visitPyteal_global_min_txn_fee_expr(self, ctx:PyTealParser.Pyteal_global_min_txn_fee_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_min_balance_expr.
    def visitPyteal_global_min_balance_expr(self, ctx:PyTealParser.Pyteal_global_min_balance_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_max_txn_life_expr.
    def visitPyteal_global_max_txn_life_expr(self, ctx:PyTealParser.Pyteal_global_max_txn_life_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_zero_address_expr.
    def visitPyteal_global_zero_address_expr(self, ctx:PyTealParser.Pyteal_global_zero_address_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_group_size_expr.
    def visitPyteal_global_group_size_expr(self, ctx:PyTealParser.Pyteal_global_group_size_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_logic_sig_version_expr.
    def visitPyteal_global_logic_sig_version_expr(self, ctx:PyTealParser.Pyteal_global_logic_sig_version_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_round_expr.
    def visitPyteal_global_round_expr(self, ctx:PyTealParser.Pyteal_global_round_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_latest_timestamp_expr.
    def visitPyteal_global_latest_timestamp_expr(self, ctx:PyTealParser.Pyteal_global_latest_timestamp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_current_application_id_expr.
    def visitPyteal_global_current_application_id_expr(self, ctx:PyTealParser.Pyteal_global_current_application_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_creator_address_expr.
    def visitPyteal_global_creator_address_expr(self, ctx:PyTealParser.Pyteal_global_creator_address_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_current_application_address_expr.
    def visitPyteal_global_current_application_address_expr(self, ctx:PyTealParser.Pyteal_global_current_application_address_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#pyteal_global_group_id_expr.
    def visitPyteal_global_group_id_expr(self, ctx:PyTealParser.Pyteal_global_group_id_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#atom_expr.
    def visitAtom_expr(self, ctx:PyTealParser.Atom_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#atom.
    def visitAtom(self, ctx:PyTealParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#name.
    def visitName(self, ctx:PyTealParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#testlist_comp.
    def visitTestlist_comp(self, ctx:PyTealParser.Testlist_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#trailer.
    def visitTrailer(self, ctx:PyTealParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#subscriptlist.
    def visitSubscriptlist(self, ctx:PyTealParser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#subscript_.
    def visitSubscript_(self, ctx:PyTealParser.Subscript_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#sliceop.
    def visitSliceop(self, ctx:PyTealParser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#exprlist.
    def visitExprlist(self, ctx:PyTealParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#testlist.
    def visitTestlist(self, ctx:PyTealParser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx:PyTealParser.DictorsetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#classdef.
    def visitClassdef(self, ctx:PyTealParser.ClassdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#arglist.
    def visitArglist(self, ctx:PyTealParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#argument.
    def visitArgument(self, ctx:PyTealParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#comp_iter.
    def visitComp_iter(self, ctx:PyTealParser.Comp_iterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#comp_for.
    def visitComp_for(self, ctx:PyTealParser.Comp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#comp_if.
    def visitComp_if(self, ctx:PyTealParser.Comp_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#encoding_decl.
    def visitEncoding_decl(self, ctx:PyTealParser.Encoding_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#yield_expr.
    def visitYield_expr(self, ctx:PyTealParser.Yield_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#yield_arg.
    def visitYield_arg(self, ctx:PyTealParser.Yield_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PyTealParser#strings.
    def visitStrings(self, ctx:PyTealParser.StringsContext):
        return self.visitChildren(ctx)



del PyTealParser