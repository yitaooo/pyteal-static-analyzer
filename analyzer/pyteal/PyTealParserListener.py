# Generated from PyTealParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PyTealParser import PyTealParser
else:
    from PyTealParser import PyTealParser

# This class defines a complete listener for a parse tree produced by PyTealParser.
class PyTealParserListener(ParseTreeListener):

    # Enter a parse tree produced by PyTealParser#file_input.
    def enterFile_input(self, ctx:PyTealParser.File_inputContext):
        pass

    # Exit a parse tree produced by PyTealParser#file_input.
    def exitFile_input(self, ctx:PyTealParser.File_inputContext):
        pass


    # Enter a parse tree produced by PyTealParser#single_input.
    def enterSingle_input(self, ctx:PyTealParser.Single_inputContext):
        pass

    # Exit a parse tree produced by PyTealParser#single_input.
    def exitSingle_input(self, ctx:PyTealParser.Single_inputContext):
        pass


    # Enter a parse tree produced by PyTealParser#eval_input.
    def enterEval_input(self, ctx:PyTealParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by PyTealParser#eval_input.
    def exitEval_input(self, ctx:PyTealParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by PyTealParser#decorator.
    def enterDecorator(self, ctx:PyTealParser.DecoratorContext):
        pass

    # Exit a parse tree produced by PyTealParser#decorator.
    def exitDecorator(self, ctx:PyTealParser.DecoratorContext):
        pass


    # Enter a parse tree produced by PyTealParser#decorators.
    def enterDecorators(self, ctx:PyTealParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by PyTealParser#decorators.
    def exitDecorators(self, ctx:PyTealParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by PyTealParser#decorated.
    def enterDecorated(self, ctx:PyTealParser.DecoratedContext):
        pass

    # Exit a parse tree produced by PyTealParser#decorated.
    def exitDecorated(self, ctx:PyTealParser.DecoratedContext):
        pass


    # Enter a parse tree produced by PyTealParser#async_funcdef.
    def enterAsync_funcdef(self, ctx:PyTealParser.Async_funcdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#async_funcdef.
    def exitAsync_funcdef(self, ctx:PyTealParser.Async_funcdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#funcdef.
    def enterFuncdef(self, ctx:PyTealParser.FuncdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#funcdef.
    def exitFuncdef(self, ctx:PyTealParser.FuncdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#parameters.
    def enterParameters(self, ctx:PyTealParser.ParametersContext):
        pass

    # Exit a parse tree produced by PyTealParser#parameters.
    def exitParameters(self, ctx:PyTealParser.ParametersContext):
        pass


    # Enter a parse tree produced by PyTealParser#typedargslist.
    def enterTypedargslist(self, ctx:PyTealParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by PyTealParser#typedargslist.
    def exitTypedargslist(self, ctx:PyTealParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by PyTealParser#tfpdef.
    def enterTfpdef(self, ctx:PyTealParser.TfpdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#tfpdef.
    def exitTfpdef(self, ctx:PyTealParser.TfpdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#varargslist.
    def enterVarargslist(self, ctx:PyTealParser.VarargslistContext):
        pass

    # Exit a parse tree produced by PyTealParser#varargslist.
    def exitVarargslist(self, ctx:PyTealParser.VarargslistContext):
        pass


    # Enter a parse tree produced by PyTealParser#vfpdef.
    def enterVfpdef(self, ctx:PyTealParser.VfpdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#vfpdef.
    def exitVfpdef(self, ctx:PyTealParser.VfpdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#stmt.
    def enterStmt(self, ctx:PyTealParser.StmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#stmt.
    def exitStmt(self, ctx:PyTealParser.StmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#simple_stmts.
    def enterSimple_stmts(self, ctx:PyTealParser.Simple_stmtsContext):
        pass

    # Exit a parse tree produced by PyTealParser#simple_stmts.
    def exitSimple_stmts(self, ctx:PyTealParser.Simple_stmtsContext):
        pass


    # Enter a parse tree produced by PyTealParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PyTealParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PyTealParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#expr_stmt.
    def enterExpr_stmt(self, ctx:PyTealParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#expr_stmt.
    def exitExpr_stmt(self, ctx:PyTealParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#annassign.
    def enterAnnassign(self, ctx:PyTealParser.AnnassignContext):
        pass

    # Exit a parse tree produced by PyTealParser#annassign.
    def exitAnnassign(self, ctx:PyTealParser.AnnassignContext):
        pass


    # Enter a parse tree produced by PyTealParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:PyTealParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:PyTealParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#augassign.
    def enterAugassign(self, ctx:PyTealParser.AugassignContext):
        pass

    # Exit a parse tree produced by PyTealParser#augassign.
    def exitAugassign(self, ctx:PyTealParser.AugassignContext):
        pass


    # Enter a parse tree produced by PyTealParser#del_stmt.
    def enterDel_stmt(self, ctx:PyTealParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#del_stmt.
    def exitDel_stmt(self, ctx:PyTealParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#pass_stmt.
    def enterPass_stmt(self, ctx:PyTealParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#pass_stmt.
    def exitPass_stmt(self, ctx:PyTealParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#flow_stmt.
    def enterFlow_stmt(self, ctx:PyTealParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#flow_stmt.
    def exitFlow_stmt(self, ctx:PyTealParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#break_stmt.
    def enterBreak_stmt(self, ctx:PyTealParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#break_stmt.
    def exitBreak_stmt(self, ctx:PyTealParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#continue_stmt.
    def enterContinue_stmt(self, ctx:PyTealParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#continue_stmt.
    def exitContinue_stmt(self, ctx:PyTealParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#return_stmt.
    def enterReturn_stmt(self, ctx:PyTealParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#return_stmt.
    def exitReturn_stmt(self, ctx:PyTealParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#yield_stmt.
    def enterYield_stmt(self, ctx:PyTealParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#yield_stmt.
    def exitYield_stmt(self, ctx:PyTealParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#raise_stmt.
    def enterRaise_stmt(self, ctx:PyTealParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#raise_stmt.
    def exitRaise_stmt(self, ctx:PyTealParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#import_stmt.
    def enterImport_stmt(self, ctx:PyTealParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#import_stmt.
    def exitImport_stmt(self, ctx:PyTealParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#import_name.
    def enterImport_name(self, ctx:PyTealParser.Import_nameContext):
        pass

    # Exit a parse tree produced by PyTealParser#import_name.
    def exitImport_name(self, ctx:PyTealParser.Import_nameContext):
        pass


    # Enter a parse tree produced by PyTealParser#import_from.
    def enterImport_from(self, ctx:PyTealParser.Import_fromContext):
        pass

    # Exit a parse tree produced by PyTealParser#import_from.
    def exitImport_from(self, ctx:PyTealParser.Import_fromContext):
        pass


    # Enter a parse tree produced by PyTealParser#import_as_name.
    def enterImport_as_name(self, ctx:PyTealParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by PyTealParser#import_as_name.
    def exitImport_as_name(self, ctx:PyTealParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by PyTealParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:PyTealParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by PyTealParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:PyTealParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by PyTealParser#import_as_names.
    def enterImport_as_names(self, ctx:PyTealParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by PyTealParser#import_as_names.
    def exitImport_as_names(self, ctx:PyTealParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by PyTealParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:PyTealParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by PyTealParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:PyTealParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by PyTealParser#dotted_name.
    def enterDotted_name(self, ctx:PyTealParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by PyTealParser#dotted_name.
    def exitDotted_name(self, ctx:PyTealParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by PyTealParser#global_stmt.
    def enterGlobal_stmt(self, ctx:PyTealParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#global_stmt.
    def exitGlobal_stmt(self, ctx:PyTealParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:PyTealParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:PyTealParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#assert_stmt.
    def enterAssert_stmt(self, ctx:PyTealParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#assert_stmt.
    def exitAssert_stmt(self, ctx:PyTealParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#compound_stmt.
    def enterCompound_stmt(self, ctx:PyTealParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#compound_stmt.
    def exitCompound_stmt(self, ctx:PyTealParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#async_stmt.
    def enterAsync_stmt(self, ctx:PyTealParser.Async_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#async_stmt.
    def exitAsync_stmt(self, ctx:PyTealParser.Async_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#if_stmt.
    def enterIf_stmt(self, ctx:PyTealParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#if_stmt.
    def exitIf_stmt(self, ctx:PyTealParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#while_stmt.
    def enterWhile_stmt(self, ctx:PyTealParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#while_stmt.
    def exitWhile_stmt(self, ctx:PyTealParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#for_stmt.
    def enterFor_stmt(self, ctx:PyTealParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#for_stmt.
    def exitFor_stmt(self, ctx:PyTealParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#try_stmt.
    def enterTry_stmt(self, ctx:PyTealParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#try_stmt.
    def exitTry_stmt(self, ctx:PyTealParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#with_stmt.
    def enterWith_stmt(self, ctx:PyTealParser.With_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#with_stmt.
    def exitWith_stmt(self, ctx:PyTealParser.With_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#with_item.
    def enterWith_item(self, ctx:PyTealParser.With_itemContext):
        pass

    # Exit a parse tree produced by PyTealParser#with_item.
    def exitWith_item(self, ctx:PyTealParser.With_itemContext):
        pass


    # Enter a parse tree produced by PyTealParser#except_clause.
    def enterExcept_clause(self, ctx:PyTealParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by PyTealParser#except_clause.
    def exitExcept_clause(self, ctx:PyTealParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by PyTealParser#block.
    def enterBlock(self, ctx:PyTealParser.BlockContext):
        pass

    # Exit a parse tree produced by PyTealParser#block.
    def exitBlock(self, ctx:PyTealParser.BlockContext):
        pass


    # Enter a parse tree produced by PyTealParser#match_stmt.
    def enterMatch_stmt(self, ctx:PyTealParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by PyTealParser#match_stmt.
    def exitMatch_stmt(self, ctx:PyTealParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by PyTealParser#subject_expr.
    def enterSubject_expr(self, ctx:PyTealParser.Subject_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#subject_expr.
    def exitSubject_expr(self, ctx:PyTealParser.Subject_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#star_named_expressions.
    def enterStar_named_expressions(self, ctx:PyTealParser.Star_named_expressionsContext):
        pass

    # Exit a parse tree produced by PyTealParser#star_named_expressions.
    def exitStar_named_expressions(self, ctx:PyTealParser.Star_named_expressionsContext):
        pass


    # Enter a parse tree produced by PyTealParser#star_named_expression.
    def enterStar_named_expression(self, ctx:PyTealParser.Star_named_expressionContext):
        pass

    # Exit a parse tree produced by PyTealParser#star_named_expression.
    def exitStar_named_expression(self, ctx:PyTealParser.Star_named_expressionContext):
        pass


    # Enter a parse tree produced by PyTealParser#case_block.
    def enterCase_block(self, ctx:PyTealParser.Case_blockContext):
        pass

    # Exit a parse tree produced by PyTealParser#case_block.
    def exitCase_block(self, ctx:PyTealParser.Case_blockContext):
        pass


    # Enter a parse tree produced by PyTealParser#guard.
    def enterGuard(self, ctx:PyTealParser.GuardContext):
        pass

    # Exit a parse tree produced by PyTealParser#guard.
    def exitGuard(self, ctx:PyTealParser.GuardContext):
        pass


    # Enter a parse tree produced by PyTealParser#patterns.
    def enterPatterns(self, ctx:PyTealParser.PatternsContext):
        pass

    # Exit a parse tree produced by PyTealParser#patterns.
    def exitPatterns(self, ctx:PyTealParser.PatternsContext):
        pass


    # Enter a parse tree produced by PyTealParser#pattern.
    def enterPattern(self, ctx:PyTealParser.PatternContext):
        pass

    # Exit a parse tree produced by PyTealParser#pattern.
    def exitPattern(self, ctx:PyTealParser.PatternContext):
        pass


    # Enter a parse tree produced by PyTealParser#as_pattern.
    def enterAs_pattern(self, ctx:PyTealParser.As_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#as_pattern.
    def exitAs_pattern(self, ctx:PyTealParser.As_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#or_pattern.
    def enterOr_pattern(self, ctx:PyTealParser.Or_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#or_pattern.
    def exitOr_pattern(self, ctx:PyTealParser.Or_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#closed_pattern.
    def enterClosed_pattern(self, ctx:PyTealParser.Closed_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#closed_pattern.
    def exitClosed_pattern(self, ctx:PyTealParser.Closed_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#literal_pattern.
    def enterLiteral_pattern(self, ctx:PyTealParser.Literal_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#literal_pattern.
    def exitLiteral_pattern(self, ctx:PyTealParser.Literal_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#literal_expr.
    def enterLiteral_expr(self, ctx:PyTealParser.Literal_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#literal_expr.
    def exitLiteral_expr(self, ctx:PyTealParser.Literal_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#complex_number.
    def enterComplex_number(self, ctx:PyTealParser.Complex_numberContext):
        pass

    # Exit a parse tree produced by PyTealParser#complex_number.
    def exitComplex_number(self, ctx:PyTealParser.Complex_numberContext):
        pass


    # Enter a parse tree produced by PyTealParser#signed_number.
    def enterSigned_number(self, ctx:PyTealParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by PyTealParser#signed_number.
    def exitSigned_number(self, ctx:PyTealParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by PyTealParser#signed_real_number.
    def enterSigned_real_number(self, ctx:PyTealParser.Signed_real_numberContext):
        pass

    # Exit a parse tree produced by PyTealParser#signed_real_number.
    def exitSigned_real_number(self, ctx:PyTealParser.Signed_real_numberContext):
        pass


    # Enter a parse tree produced by PyTealParser#real_number.
    def enterReal_number(self, ctx:PyTealParser.Real_numberContext):
        pass

    # Exit a parse tree produced by PyTealParser#real_number.
    def exitReal_number(self, ctx:PyTealParser.Real_numberContext):
        pass


    # Enter a parse tree produced by PyTealParser#imaginary_number.
    def enterImaginary_number(self, ctx:PyTealParser.Imaginary_numberContext):
        pass

    # Exit a parse tree produced by PyTealParser#imaginary_number.
    def exitImaginary_number(self, ctx:PyTealParser.Imaginary_numberContext):
        pass


    # Enter a parse tree produced by PyTealParser#capture_pattern.
    def enterCapture_pattern(self, ctx:PyTealParser.Capture_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#capture_pattern.
    def exitCapture_pattern(self, ctx:PyTealParser.Capture_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#pattern_capture_target.
    def enterPattern_capture_target(self, ctx:PyTealParser.Pattern_capture_targetContext):
        pass

    # Exit a parse tree produced by PyTealParser#pattern_capture_target.
    def exitPattern_capture_target(self, ctx:PyTealParser.Pattern_capture_targetContext):
        pass


    # Enter a parse tree produced by PyTealParser#wildcard_pattern.
    def enterWildcard_pattern(self, ctx:PyTealParser.Wildcard_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#wildcard_pattern.
    def exitWildcard_pattern(self, ctx:PyTealParser.Wildcard_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#value_pattern.
    def enterValue_pattern(self, ctx:PyTealParser.Value_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#value_pattern.
    def exitValue_pattern(self, ctx:PyTealParser.Value_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#attr.
    def enterAttr(self, ctx:PyTealParser.AttrContext):
        pass

    # Exit a parse tree produced by PyTealParser#attr.
    def exitAttr(self, ctx:PyTealParser.AttrContext):
        pass


    # Enter a parse tree produced by PyTealParser#name_or_attr.
    def enterName_or_attr(self, ctx:PyTealParser.Name_or_attrContext):
        pass

    # Exit a parse tree produced by PyTealParser#name_or_attr.
    def exitName_or_attr(self, ctx:PyTealParser.Name_or_attrContext):
        pass


    # Enter a parse tree produced by PyTealParser#group_pattern.
    def enterGroup_pattern(self, ctx:PyTealParser.Group_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#group_pattern.
    def exitGroup_pattern(self, ctx:PyTealParser.Group_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#sequence_pattern.
    def enterSequence_pattern(self, ctx:PyTealParser.Sequence_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#sequence_pattern.
    def exitSequence_pattern(self, ctx:PyTealParser.Sequence_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#open_sequence_pattern.
    def enterOpen_sequence_pattern(self, ctx:PyTealParser.Open_sequence_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#open_sequence_pattern.
    def exitOpen_sequence_pattern(self, ctx:PyTealParser.Open_sequence_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#maybe_sequence_pattern.
    def enterMaybe_sequence_pattern(self, ctx:PyTealParser.Maybe_sequence_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#maybe_sequence_pattern.
    def exitMaybe_sequence_pattern(self, ctx:PyTealParser.Maybe_sequence_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#maybe_star_pattern.
    def enterMaybe_star_pattern(self, ctx:PyTealParser.Maybe_star_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#maybe_star_pattern.
    def exitMaybe_star_pattern(self, ctx:PyTealParser.Maybe_star_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#star_pattern.
    def enterStar_pattern(self, ctx:PyTealParser.Star_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#star_pattern.
    def exitStar_pattern(self, ctx:PyTealParser.Star_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#mapping_pattern.
    def enterMapping_pattern(self, ctx:PyTealParser.Mapping_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#mapping_pattern.
    def exitMapping_pattern(self, ctx:PyTealParser.Mapping_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#items_pattern.
    def enterItems_pattern(self, ctx:PyTealParser.Items_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#items_pattern.
    def exitItems_pattern(self, ctx:PyTealParser.Items_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#key_value_pattern.
    def enterKey_value_pattern(self, ctx:PyTealParser.Key_value_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#key_value_pattern.
    def exitKey_value_pattern(self, ctx:PyTealParser.Key_value_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#double_star_pattern.
    def enterDouble_star_pattern(self, ctx:PyTealParser.Double_star_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#double_star_pattern.
    def exitDouble_star_pattern(self, ctx:PyTealParser.Double_star_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#class_pattern.
    def enterClass_pattern(self, ctx:PyTealParser.Class_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#class_pattern.
    def exitClass_pattern(self, ctx:PyTealParser.Class_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#positional_patterns.
    def enterPositional_patterns(self, ctx:PyTealParser.Positional_patternsContext):
        pass

    # Exit a parse tree produced by PyTealParser#positional_patterns.
    def exitPositional_patterns(self, ctx:PyTealParser.Positional_patternsContext):
        pass


    # Enter a parse tree produced by PyTealParser#keyword_patterns.
    def enterKeyword_patterns(self, ctx:PyTealParser.Keyword_patternsContext):
        pass

    # Exit a parse tree produced by PyTealParser#keyword_patterns.
    def exitKeyword_patterns(self, ctx:PyTealParser.Keyword_patternsContext):
        pass


    # Enter a parse tree produced by PyTealParser#keyword_pattern.
    def enterKeyword_pattern(self, ctx:PyTealParser.Keyword_patternContext):
        pass

    # Exit a parse tree produced by PyTealParser#keyword_pattern.
    def exitKeyword_pattern(self, ctx:PyTealParser.Keyword_patternContext):
        pass


    # Enter a parse tree produced by PyTealParser#test.
    def enterTest(self, ctx:PyTealParser.TestContext):
        pass

    # Exit a parse tree produced by PyTealParser#test.
    def exitTest(self, ctx:PyTealParser.TestContext):
        pass


    # Enter a parse tree produced by PyTealParser#test_nocond.
    def enterTest_nocond(self, ctx:PyTealParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by PyTealParser#test_nocond.
    def exitTest_nocond(self, ctx:PyTealParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by PyTealParser#lambdef.
    def enterLambdef(self, ctx:PyTealParser.LambdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#lambdef.
    def exitLambdef(self, ctx:PyTealParser.LambdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:PyTealParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by PyTealParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:PyTealParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by PyTealParser#or_test.
    def enterOr_test(self, ctx:PyTealParser.Or_testContext):
        pass

    # Exit a parse tree produced by PyTealParser#or_test.
    def exitOr_test(self, ctx:PyTealParser.Or_testContext):
        pass


    # Enter a parse tree produced by PyTealParser#and_test.
    def enterAnd_test(self, ctx:PyTealParser.And_testContext):
        pass

    # Exit a parse tree produced by PyTealParser#and_test.
    def exitAnd_test(self, ctx:PyTealParser.And_testContext):
        pass


    # Enter a parse tree produced by PyTealParser#not_test.
    def enterNot_test(self, ctx:PyTealParser.Not_testContext):
        pass

    # Exit a parse tree produced by PyTealParser#not_test.
    def exitNot_test(self, ctx:PyTealParser.Not_testContext):
        pass


    # Enter a parse tree produced by PyTealParser#comparison.
    def enterComparison(self, ctx:PyTealParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PyTealParser#comparison.
    def exitComparison(self, ctx:PyTealParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PyTealParser#comp_op.
    def enterComp_op(self, ctx:PyTealParser.Comp_opContext):
        pass

    # Exit a parse tree produced by PyTealParser#comp_op.
    def exitComp_op(self, ctx:PyTealParser.Comp_opContext):
        pass


    # Enter a parse tree produced by PyTealParser#star_expr.
    def enterStar_expr(self, ctx:PyTealParser.Star_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#star_expr.
    def exitStar_expr(self, ctx:PyTealParser.Star_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#expr.
    def enterExpr(self, ctx:PyTealParser.ExprContext):
        pass

    # Exit a parse tree produced by PyTealParser#expr.
    def exitExpr(self, ctx:PyTealParser.ExprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_data_expr.
    def enterPyteal_data_expr(self, ctx:PyTealParser.Pyteal_data_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_data_expr.
    def exitPyteal_data_expr(self, ctx:PyTealParser.Pyteal_data_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_integers_expr.
    def enterPyteal_integers_expr(self, ctx:PyTealParser.Pyteal_integers_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_integers_expr.
    def exitPyteal_integers_expr(self, ctx:PyTealParser.Pyteal_integers_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_expr.
    def enterPyteal_bytes_expr(self, ctx:PyTealParser.Pyteal_bytes_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_expr.
    def exitPyteal_bytes_expr(self, ctx:PyTealParser.Pyteal_bytes_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_base.
    def enterPyteal_bytes_base(self, ctx:PyTealParser.Pyteal_bytes_baseContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_base.
    def exitPyteal_bytes_base(self, ctx:PyTealParser.Pyteal_bytes_baseContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_conversion_expr.
    def enterPyteal_conversion_expr(self, ctx:PyTealParser.Pyteal_conversion_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_conversion_expr.
    def exitPyteal_conversion_expr(self, ctx:PyTealParser.Pyteal_conversion_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_arithmetic_operations.
    def enterPyteal_arithmetic_operations(self, ctx:PyTealParser.Pyteal_arithmetic_operationsContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_arithmetic_operations.
    def exitPyteal_arithmetic_operations(self, ctx:PyTealParser.Pyteal_arithmetic_operationsContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_comparison.
    def enterPyteal_comparison(self, ctx:PyTealParser.Pyteal_comparisonContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_comparison.
    def exitPyteal_comparison(self, ctx:PyTealParser.Pyteal_comparisonContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_comp_op.
    def enterPyteal_comp_op(self, ctx:PyTealParser.Pyteal_comp_opContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_comp_op.
    def exitPyteal_comp_op(self, ctx:PyTealParser.Pyteal_comp_opContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_comparison.
    def enterPyteal_bytes_comparison(self, ctx:PyTealParser.Pyteal_bytes_comparisonContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_comparison.
    def exitPyteal_bytes_comparison(self, ctx:PyTealParser.Pyteal_bytes_comparisonContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_comp_op.
    def enterPyteal_bytes_comp_op(self, ctx:PyTealParser.Pyteal_bytes_comp_opContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_comp_op.
    def exitPyteal_bytes_comp_op(self, ctx:PyTealParser.Pyteal_bytes_comp_opContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_or_expr.
    def enterPyteal_or_expr(self, ctx:PyTealParser.Pyteal_or_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_or_expr.
    def exitPyteal_or_expr(self, ctx:PyTealParser.Pyteal_or_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_and_expr.
    def enterPyteal_and_expr(self, ctx:PyTealParser.Pyteal_and_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_and_expr.
    def exitPyteal_and_expr(self, ctx:PyTealParser.Pyteal_and_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_not_expr.
    def enterPyteal_not_expr(self, ctx:PyTealParser.Pyteal_not_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_not_expr.
    def exitPyteal_not_expr(self, ctx:PyTealParser.Pyteal_not_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_exp_expr.
    def enterPyteal_exp_expr(self, ctx:PyTealParser.Pyteal_exp_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_exp_expr.
    def exitPyteal_exp_expr(self, ctx:PyTealParser.Pyteal_exp_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_add_expr.
    def enterPyteal_add_expr(self, ctx:PyTealParser.Pyteal_add_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_add_expr.
    def exitPyteal_add_expr(self, ctx:PyTealParser.Pyteal_add_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_minus_expr.
    def enterPyteal_minus_expr(self, ctx:PyTealParser.Pyteal_minus_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_minus_expr.
    def exitPyteal_minus_expr(self, ctx:PyTealParser.Pyteal_minus_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bitwise_not_expr.
    def enterPyteal_bitwise_not_expr(self, ctx:PyTealParser.Pyteal_bitwise_not_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bitwise_not_expr.
    def exitPyteal_bitwise_not_expr(self, ctx:PyTealParser.Pyteal_bitwise_not_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_mul_expr.
    def enterPyteal_mul_expr(self, ctx:PyTealParser.Pyteal_mul_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_mul_expr.
    def exitPyteal_mul_expr(self, ctx:PyTealParser.Pyteal_mul_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_div_expr.
    def enterPyteal_div_expr(self, ctx:PyTealParser.Pyteal_div_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_div_expr.
    def exitPyteal_div_expr(self, ctx:PyTealParser.Pyteal_div_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_mod_expr.
    def enterPyteal_mod_expr(self, ctx:PyTealParser.Pyteal_mod_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_mod_expr.
    def exitPyteal_mod_expr(self, ctx:PyTealParser.Pyteal_mod_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bitwise_and_expr.
    def enterPyteal_bitwise_and_expr(self, ctx:PyTealParser.Pyteal_bitwise_and_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bitwise_and_expr.
    def exitPyteal_bitwise_and_expr(self, ctx:PyTealParser.Pyteal_bitwise_and_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bitwise_xor_expr.
    def enterPyteal_bitwise_xor_expr(self, ctx:PyTealParser.Pyteal_bitwise_xor_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bitwise_xor_expr.
    def exitPyteal_bitwise_xor_expr(self, ctx:PyTealParser.Pyteal_bitwise_xor_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bitwise_or_expr.
    def enterPyteal_bitwise_or_expr(self, ctx:PyTealParser.Pyteal_bitwise_or_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bitwise_or_expr.
    def exitPyteal_bitwise_or_expr(self, ctx:PyTealParser.Pyteal_bitwise_or_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_or_expr.
    def enterPyteal_bytes_or_expr(self, ctx:PyTealParser.Pyteal_bytes_or_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_or_expr.
    def exitPyteal_bytes_or_expr(self, ctx:PyTealParser.Pyteal_bytes_or_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_and_expr.
    def enterPyteal_bytes_and_expr(self, ctx:PyTealParser.Pyteal_bytes_and_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_and_expr.
    def exitPyteal_bytes_and_expr(self, ctx:PyTealParser.Pyteal_bytes_and_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_not_expr.
    def enterPyteal_bytes_not_expr(self, ctx:PyTealParser.Pyteal_bytes_not_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_not_expr.
    def exitPyteal_bytes_not_expr(self, ctx:PyTealParser.Pyteal_bytes_not_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_mul_expr.
    def enterPyteal_bytes_mul_expr(self, ctx:PyTealParser.Pyteal_bytes_mul_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_mul_expr.
    def exitPyteal_bytes_mul_expr(self, ctx:PyTealParser.Pyteal_bytes_mul_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_div_expr.
    def enterPyteal_bytes_div_expr(self, ctx:PyTealParser.Pyteal_bytes_div_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_div_expr.
    def exitPyteal_bytes_div_expr(self, ctx:PyTealParser.Pyteal_bytes_div_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_mod_expr.
    def enterPyteal_bytes_mod_expr(self, ctx:PyTealParser.Pyteal_bytes_mod_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_mod_expr.
    def exitPyteal_bytes_mod_expr(self, ctx:PyTealParser.Pyteal_bytes_mod_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_add_expr.
    def enterPyteal_bytes_add_expr(self, ctx:PyTealParser.Pyteal_bytes_add_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_add_expr.
    def exitPyteal_bytes_add_expr(self, ctx:PyTealParser.Pyteal_bytes_add_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_minus_expr.
    def enterPyteal_bytes_minus_expr(self, ctx:PyTealParser.Pyteal_bytes_minus_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_minus_expr.
    def exitPyteal_bytes_minus_expr(self, ctx:PyTealParser.Pyteal_bytes_minus_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_xor_expr.
    def enterPyteal_bytes_xor_expr(self, ctx:PyTealParser.Pyteal_bytes_xor_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_xor_expr.
    def exitPyteal_bytes_xor_expr(self, ctx:PyTealParser.Pyteal_bytes_xor_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_bytes_zero_expr.
    def enterPyteal_bytes_zero_expr(self, ctx:PyTealParser.Pyteal_bytes_zero_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_bytes_zero_expr.
    def exitPyteal_bytes_zero_expr(self, ctx:PyTealParser.Pyteal_bytes_zero_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_expr.
    def enterPyteal_txn_expr(self, ctx:PyTealParser.Pyteal_txn_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_expr.
    def exitPyteal_txn_expr(self, ctx:PyTealParser.Pyteal_txn_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_type_expr.
    def enterPyteal_txn_type_expr(self, ctx:PyTealParser.Pyteal_txn_type_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_type_expr.
    def exitPyteal_txn_type_expr(self, ctx:PyTealParser.Pyteal_txn_type_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_type_enum_expr.
    def enterPyteal_txn_type_enum_expr(self, ctx:PyTealParser.Pyteal_txn_type_enum_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_type_enum_expr.
    def exitPyteal_txn_type_enum_expr(self, ctx:PyTealParser.Pyteal_txn_type_enum_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_sender_expr.
    def enterPyteal_txn_sender_expr(self, ctx:PyTealParser.Pyteal_txn_sender_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_sender_expr.
    def exitPyteal_txn_sender_expr(self, ctx:PyTealParser.Pyteal_txn_sender_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_fee_expr.
    def enterPyteal_txn_fee_expr(self, ctx:PyTealParser.Pyteal_txn_fee_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_fee_expr.
    def exitPyteal_txn_fee_expr(self, ctx:PyTealParser.Pyteal_txn_fee_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_first_valid_expr.
    def enterPyteal_txn_first_valid_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_first_valid_expr.
    def exitPyteal_txn_first_valid_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_first_valid_time_expr.
    def enterPyteal_txn_first_valid_time_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_time_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_first_valid_time_expr.
    def exitPyteal_txn_first_valid_time_expr(self, ctx:PyTealParser.Pyteal_txn_first_valid_time_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_last_valid_expr.
    def enterPyteal_txn_last_valid_expr(self, ctx:PyTealParser.Pyteal_txn_last_valid_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_last_valid_expr.
    def exitPyteal_txn_last_valid_expr(self, ctx:PyTealParser.Pyteal_txn_last_valid_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_note_expr.
    def enterPyteal_txn_note_expr(self, ctx:PyTealParser.Pyteal_txn_note_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_note_expr.
    def exitPyteal_txn_note_expr(self, ctx:PyTealParser.Pyteal_txn_note_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_lease_expr.
    def enterPyteal_txn_lease_expr(self, ctx:PyTealParser.Pyteal_txn_lease_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_lease_expr.
    def exitPyteal_txn_lease_expr(self, ctx:PyTealParser.Pyteal_txn_lease_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_group_index_expr.
    def enterPyteal_txn_group_index_expr(self, ctx:PyTealParser.Pyteal_txn_group_index_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_group_index_expr.
    def exitPyteal_txn_group_index_expr(self, ctx:PyTealParser.Pyteal_txn_group_index_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_tx_id_expr.
    def enterPyteal_txn_tx_id_expr(self, ctx:PyTealParser.Pyteal_txn_tx_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_tx_id_expr.
    def exitPyteal_txn_tx_id_expr(self, ctx:PyTealParser.Pyteal_txn_tx_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_rekey_to_expr.
    def enterPyteal_txn_rekey_to_expr(self, ctx:PyTealParser.Pyteal_txn_rekey_to_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_rekey_to_expr.
    def exitPyteal_txn_rekey_to_expr(self, ctx:PyTealParser.Pyteal_txn_rekey_to_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_application_id_expr.
    def enterPyteal_txn_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_application_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_application_id_expr.
    def exitPyteal_txn_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_application_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_on_completion_expr.
    def enterPyteal_txn_on_completion_expr(self, ctx:PyTealParser.Pyteal_txn_on_completion_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_on_completion_expr.
    def exitPyteal_txn_on_completion_expr(self, ctx:PyTealParser.Pyteal_txn_on_completion_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_approval_program_expr.
    def enterPyteal_txn_approval_program_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_approval_program_expr.
    def exitPyteal_txn_approval_program_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_global_num_uints_expr.
    def enterPyteal_txn_global_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_uints_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_global_num_uints_expr.
    def exitPyteal_txn_global_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_uints_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_global_num_byte_slices_expr.
    def enterPyteal_txn_global_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_byte_slices_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_global_num_byte_slices_expr.
    def exitPyteal_txn_global_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_global_num_byte_slices_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_local_num_uints_expr.
    def enterPyteal_txn_local_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_uints_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_local_num_uints_expr.
    def exitPyteal_txn_local_num_uints_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_uints_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_local_num_byte_slices_expr.
    def enterPyteal_txn_local_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_byte_slices_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_local_num_byte_slices_expr.
    def exitPyteal_txn_local_num_byte_slices_expr(self, ctx:PyTealParser.Pyteal_txn_local_num_byte_slices_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_accounts_expr.
    def enterPyteal_txn_accounts_expr(self, ctx:PyTealParser.Pyteal_txn_accounts_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_accounts_expr.
    def exitPyteal_txn_accounts_expr(self, ctx:PyTealParser.Pyteal_txn_accounts_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_assets_expr.
    def enterPyteal_txn_assets_expr(self, ctx:PyTealParser.Pyteal_txn_assets_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_assets_expr.
    def exitPyteal_txn_assets_expr(self, ctx:PyTealParser.Pyteal_txn_assets_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_applications_expr.
    def enterPyteal_txn_applications_expr(self, ctx:PyTealParser.Pyteal_txn_applications_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_applications_expr.
    def exitPyteal_txn_applications_expr(self, ctx:PyTealParser.Pyteal_txn_applications_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_expr.
    def enterPyteal_txn_clear_state_program_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_expr.
    def exitPyteal_txn_clear_state_program_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_extra_program_pages_expr.
    def enterPyteal_txn_extra_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_extra_program_pages_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_extra_program_pages_expr.
    def exitPyteal_txn_extra_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_extra_program_pages_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_application_args_expr.
    def enterPyteal_txn_application_args_expr(self, ctx:PyTealParser.Pyteal_txn_application_args_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_application_args_expr.
    def exitPyteal_txn_application_args_expr(self, ctx:PyTealParser.Pyteal_txn_application_args_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_created_application_id_expr.
    def enterPyteal_txn_created_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_application_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_created_application_id_expr.
    def exitPyteal_txn_created_application_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_application_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_logs_expr.
    def enterPyteal_txn_logs_expr(self, ctx:PyTealParser.Pyteal_txn_logs_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_logs_expr.
    def exitPyteal_txn_logs_expr(self, ctx:PyTealParser.Pyteal_txn_logs_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_last_log_expr.
    def enterPyteal_txn_last_log_expr(self, ctx:PyTealParser.Pyteal_txn_last_log_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_last_log_expr.
    def exitPyteal_txn_last_log_expr(self, ctx:PyTealParser.Pyteal_txn_last_log_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_approval_program_pages_expr.
    def enterPyteal_txn_approval_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_pages_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_approval_program_pages_expr.
    def exitPyteal_txn_approval_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_approval_program_pages_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_pages_expr.
    def enterPyteal_txn_clear_state_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_pages_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_clear_state_program_pages_expr.
    def exitPyteal_txn_clear_state_program_pages_expr(self, ctx:PyTealParser.Pyteal_txn_clear_state_program_pages_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_expr.
    def enterPyteal_txn_config_asset_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_expr.
    def exitPyteal_txn_config_asset_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_total_expr.
    def enterPyteal_txn_config_asset_total_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_total_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_total_expr.
    def exitPyteal_txn_config_asset_total_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_total_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_decimals_expr.
    def enterPyteal_txn_config_asset_decimals_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_decimals_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_decimals_expr.
    def exitPyteal_txn_config_asset_decimals_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_decimals_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_default_frozen_expr.
    def enterPyteal_txn_config_asset_default_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_default_frozen_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_default_frozen_expr.
    def exitPyteal_txn_config_asset_default_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_default_frozen_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_unit_name_expr.
    def enterPyteal_txn_config_asset_unit_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_unit_name_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_unit_name_expr.
    def exitPyteal_txn_config_asset_unit_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_unit_name_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_name_expr.
    def enterPyteal_txn_config_asset_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_name_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_name_expr.
    def exitPyteal_txn_config_asset_name_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_name_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_url_expr.
    def enterPyteal_txn_config_asset_url_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_url_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_url_expr.
    def exitPyteal_txn_config_asset_url_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_url_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_metadata_hash_expr.
    def enterPyteal_txn_config_asset_metadata_hash_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_metadata_hash_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_metadata_hash_expr.
    def exitPyteal_txn_config_asset_metadata_hash_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_metadata_hash_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_manager_expr.
    def enterPyteal_txn_config_asset_manager_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_manager_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_manager_expr.
    def exitPyteal_txn_config_asset_manager_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_manager_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_reserve_expr.
    def enterPyteal_txn_config_asset_reserve_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_reserve_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_reserve_expr.
    def exitPyteal_txn_config_asset_reserve_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_reserve_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_freeze_expr.
    def enterPyteal_txn_config_asset_freeze_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_freeze_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_freeze_expr.
    def exitPyteal_txn_config_asset_freeze_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_freeze_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_config_asset_clawback_expr.
    def enterPyteal_txn_config_asset_clawback_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_clawback_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_config_asset_clawback_expr.
    def exitPyteal_txn_config_asset_clawback_expr(self, ctx:PyTealParser.Pyteal_txn_config_asset_clawback_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_created_asset_id_expr.
    def enterPyteal_txn_created_asset_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_asset_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_created_asset_id_expr.
    def exitPyteal_txn_created_asset_id_expr(self, ctx:PyTealParser.Pyteal_txn_created_asset_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_expr.
    def enterPyteal_txn_freeze_asset_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_expr.
    def exitPyteal_txn_freeze_asset_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_account_expr.
    def enterPyteal_txn_freeze_asset_account_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_account_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_account_expr.
    def exitPyteal_txn_freeze_asset_account_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_account_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_frozen_expr.
    def enterPyteal_txn_freeze_asset_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_frozen_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_freeze_asset_frozen_expr.
    def exitPyteal_txn_freeze_asset_frozen_expr(self, ctx:PyTealParser.Pyteal_txn_freeze_asset_frozen_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_xfer_asset_expr.
    def enterPyteal_txn_xfer_asset_expr(self, ctx:PyTealParser.Pyteal_txn_xfer_asset_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_xfer_asset_expr.
    def exitPyteal_txn_xfer_asset_expr(self, ctx:PyTealParser.Pyteal_txn_xfer_asset_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_asset_amount_expr.
    def enterPyteal_txn_asset_amount_expr(self, ctx:PyTealParser.Pyteal_txn_asset_amount_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_asset_amount_expr.
    def exitPyteal_txn_asset_amount_expr(self, ctx:PyTealParser.Pyteal_txn_asset_amount_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_asset_sender_expr.
    def enterPyteal_txn_asset_sender_expr(self, ctx:PyTealParser.Pyteal_txn_asset_sender_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_asset_sender_expr.
    def exitPyteal_txn_asset_sender_expr(self, ctx:PyTealParser.Pyteal_txn_asset_sender_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_asset_receiver_expr.
    def enterPyteal_txn_asset_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_asset_receiver_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_asset_receiver_expr.
    def exitPyteal_txn_asset_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_asset_receiver_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_asset_close_to_expr.
    def enterPyteal_txn_asset_close_to_expr(self, ctx:PyTealParser.Pyteal_txn_asset_close_to_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_asset_close_to_expr.
    def exitPyteal_txn_asset_close_to_expr(self, ctx:PyTealParser.Pyteal_txn_asset_close_to_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_vote_pk_expr.
    def enterPyteal_txn_vote_pk_expr(self, ctx:PyTealParser.Pyteal_txn_vote_pk_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_vote_pk_expr.
    def exitPyteal_txn_vote_pk_expr(self, ctx:PyTealParser.Pyteal_txn_vote_pk_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_selection_pk_expr.
    def enterPyteal_txn_selection_pk_expr(self, ctx:PyTealParser.Pyteal_txn_selection_pk_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_selection_pk_expr.
    def exitPyteal_txn_selection_pk_expr(self, ctx:PyTealParser.Pyteal_txn_selection_pk_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_state_proof_pk_expr.
    def enterPyteal_txn_state_proof_pk_expr(self, ctx:PyTealParser.Pyteal_txn_state_proof_pk_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_state_proof_pk_expr.
    def exitPyteal_txn_state_proof_pk_expr(self, ctx:PyTealParser.Pyteal_txn_state_proof_pk_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_vote_first_expr.
    def enterPyteal_txn_vote_first_expr(self, ctx:PyTealParser.Pyteal_txn_vote_first_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_vote_first_expr.
    def exitPyteal_txn_vote_first_expr(self, ctx:PyTealParser.Pyteal_txn_vote_first_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_vote_last_expr.
    def enterPyteal_txn_vote_last_expr(self, ctx:PyTealParser.Pyteal_txn_vote_last_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_vote_last_expr.
    def exitPyteal_txn_vote_last_expr(self, ctx:PyTealParser.Pyteal_txn_vote_last_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_vote_key_dilution_expr.
    def enterPyteal_txn_vote_key_dilution_expr(self, ctx:PyTealParser.Pyteal_txn_vote_key_dilution_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_vote_key_dilution_expr.
    def exitPyteal_txn_vote_key_dilution_expr(self, ctx:PyTealParser.Pyteal_txn_vote_key_dilution_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_nonparticipation_expr.
    def enterPyteal_txn_nonparticipation_expr(self, ctx:PyTealParser.Pyteal_txn_nonparticipation_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_nonparticipation_expr.
    def exitPyteal_txn_nonparticipation_expr(self, ctx:PyTealParser.Pyteal_txn_nonparticipation_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_receiver_expr.
    def enterPyteal_txn_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_receiver_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_receiver_expr.
    def exitPyteal_txn_receiver_expr(self, ctx:PyTealParser.Pyteal_txn_receiver_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_amount_expr.
    def enterPyteal_txn_amount_expr(self, ctx:PyTealParser.Pyteal_txn_amount_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_amount_expr.
    def exitPyteal_txn_amount_expr(self, ctx:PyTealParser.Pyteal_txn_amount_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txn_close_remainder_to_expr.
    def enterPyteal_txn_close_remainder_to_expr(self, ctx:PyTealParser.Pyteal_txn_close_remainder_to_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txn_close_remainder_to_expr.
    def exitPyteal_txn_close_remainder_to_expr(self, ctx:PyTealParser.Pyteal_txn_close_remainder_to_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_Unknown_expr.
    def enterPyteal_txntype_Unknown_expr(self, ctx:PyTealParser.Pyteal_txntype_Unknown_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_Unknown_expr.
    def exitPyteal_txntype_Unknown_expr(self, ctx:PyTealParser.Pyteal_txntype_Unknown_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_Payment_expr.
    def enterPyteal_txntype_Payment_expr(self, ctx:PyTealParser.Pyteal_txntype_Payment_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_Payment_expr.
    def exitPyteal_txntype_Payment_expr(self, ctx:PyTealParser.Pyteal_txntype_Payment_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_KeyRegistration_expr.
    def enterPyteal_txntype_KeyRegistration_expr(self, ctx:PyTealParser.Pyteal_txntype_KeyRegistration_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_KeyRegistration_expr.
    def exitPyteal_txntype_KeyRegistration_expr(self, ctx:PyTealParser.Pyteal_txntype_KeyRegistration_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_AssetConfig_expr.
    def enterPyteal_txntype_AssetConfig_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetConfig_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_AssetConfig_expr.
    def exitPyteal_txntype_AssetConfig_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetConfig_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_AssetTransfer_expr.
    def enterPyteal_txntype_AssetTransfer_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetTransfer_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_AssetTransfer_expr.
    def exitPyteal_txntype_AssetTransfer_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetTransfer_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_AssetFreeze_expr.
    def enterPyteal_txntype_AssetFreeze_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetFreeze_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_AssetFreeze_expr.
    def exitPyteal_txntype_AssetFreeze_expr(self, ctx:PyTealParser.Pyteal_txntype_AssetFreeze_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_txntype_ApplicationCall_expr.
    def enterPyteal_txntype_ApplicationCall_expr(self, ctx:PyTealParser.Pyteal_txntype_ApplicationCall_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_txntype_ApplicationCall_expr.
    def exitPyteal_txntype_ApplicationCall_expr(self, ctx:PyTealParser.Pyteal_txntype_ApplicationCall_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_min_txn_fee_expr.
    def enterPyteal_global_min_txn_fee_expr(self, ctx:PyTealParser.Pyteal_global_min_txn_fee_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_min_txn_fee_expr.
    def exitPyteal_global_min_txn_fee_expr(self, ctx:PyTealParser.Pyteal_global_min_txn_fee_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_min_balance_expr.
    def enterPyteal_global_min_balance_expr(self, ctx:PyTealParser.Pyteal_global_min_balance_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_min_balance_expr.
    def exitPyteal_global_min_balance_expr(self, ctx:PyTealParser.Pyteal_global_min_balance_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_max_txn_life_expr.
    def enterPyteal_global_max_txn_life_expr(self, ctx:PyTealParser.Pyteal_global_max_txn_life_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_max_txn_life_expr.
    def exitPyteal_global_max_txn_life_expr(self, ctx:PyTealParser.Pyteal_global_max_txn_life_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_zero_address_expr.
    def enterPyteal_global_zero_address_expr(self, ctx:PyTealParser.Pyteal_global_zero_address_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_zero_address_expr.
    def exitPyteal_global_zero_address_expr(self, ctx:PyTealParser.Pyteal_global_zero_address_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_group_size_expr.
    def enterPyteal_global_group_size_expr(self, ctx:PyTealParser.Pyteal_global_group_size_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_group_size_expr.
    def exitPyteal_global_group_size_expr(self, ctx:PyTealParser.Pyteal_global_group_size_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_logic_sig_version_expr.
    def enterPyteal_global_logic_sig_version_expr(self, ctx:PyTealParser.Pyteal_global_logic_sig_version_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_logic_sig_version_expr.
    def exitPyteal_global_logic_sig_version_expr(self, ctx:PyTealParser.Pyteal_global_logic_sig_version_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_round_expr.
    def enterPyteal_global_round_expr(self, ctx:PyTealParser.Pyteal_global_round_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_round_expr.
    def exitPyteal_global_round_expr(self, ctx:PyTealParser.Pyteal_global_round_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_latest_timestamp_expr.
    def enterPyteal_global_latest_timestamp_expr(self, ctx:PyTealParser.Pyteal_global_latest_timestamp_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_latest_timestamp_expr.
    def exitPyteal_global_latest_timestamp_expr(self, ctx:PyTealParser.Pyteal_global_latest_timestamp_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_current_application_id_expr.
    def enterPyteal_global_current_application_id_expr(self, ctx:PyTealParser.Pyteal_global_current_application_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_current_application_id_expr.
    def exitPyteal_global_current_application_id_expr(self, ctx:PyTealParser.Pyteal_global_current_application_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_creator_address_expr.
    def enterPyteal_global_creator_address_expr(self, ctx:PyTealParser.Pyteal_global_creator_address_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_creator_address_expr.
    def exitPyteal_global_creator_address_expr(self, ctx:PyTealParser.Pyteal_global_creator_address_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_current_application_address_expr.
    def enterPyteal_global_current_application_address_expr(self, ctx:PyTealParser.Pyteal_global_current_application_address_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_current_application_address_expr.
    def exitPyteal_global_current_application_address_expr(self, ctx:PyTealParser.Pyteal_global_current_application_address_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#pyteal_global_group_id_expr.
    def enterPyteal_global_group_id_expr(self, ctx:PyTealParser.Pyteal_global_group_id_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#pyteal_global_group_id_expr.
    def exitPyteal_global_group_id_expr(self, ctx:PyTealParser.Pyteal_global_group_id_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#atom_expr.
    def enterAtom_expr(self, ctx:PyTealParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#atom_expr.
    def exitAtom_expr(self, ctx:PyTealParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#atom.
    def enterAtom(self, ctx:PyTealParser.AtomContext):
        pass

    # Exit a parse tree produced by PyTealParser#atom.
    def exitAtom(self, ctx:PyTealParser.AtomContext):
        pass


    # Enter a parse tree produced by PyTealParser#name.
    def enterName(self, ctx:PyTealParser.NameContext):
        pass

    # Exit a parse tree produced by PyTealParser#name.
    def exitName(self, ctx:PyTealParser.NameContext):
        pass


    # Enter a parse tree produced by PyTealParser#testlist_comp.
    def enterTestlist_comp(self, ctx:PyTealParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by PyTealParser#testlist_comp.
    def exitTestlist_comp(self, ctx:PyTealParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by PyTealParser#trailer.
    def enterTrailer(self, ctx:PyTealParser.TrailerContext):
        pass

    # Exit a parse tree produced by PyTealParser#trailer.
    def exitTrailer(self, ctx:PyTealParser.TrailerContext):
        pass


    # Enter a parse tree produced by PyTealParser#subscriptlist.
    def enterSubscriptlist(self, ctx:PyTealParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by PyTealParser#subscriptlist.
    def exitSubscriptlist(self, ctx:PyTealParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by PyTealParser#subscript_.
    def enterSubscript_(self, ctx:PyTealParser.Subscript_Context):
        pass

    # Exit a parse tree produced by PyTealParser#subscript_.
    def exitSubscript_(self, ctx:PyTealParser.Subscript_Context):
        pass


    # Enter a parse tree produced by PyTealParser#sliceop.
    def enterSliceop(self, ctx:PyTealParser.SliceopContext):
        pass

    # Exit a parse tree produced by PyTealParser#sliceop.
    def exitSliceop(self, ctx:PyTealParser.SliceopContext):
        pass


    # Enter a parse tree produced by PyTealParser#exprlist.
    def enterExprlist(self, ctx:PyTealParser.ExprlistContext):
        pass

    # Exit a parse tree produced by PyTealParser#exprlist.
    def exitExprlist(self, ctx:PyTealParser.ExprlistContext):
        pass


    # Enter a parse tree produced by PyTealParser#testlist.
    def enterTestlist(self, ctx:PyTealParser.TestlistContext):
        pass

    # Exit a parse tree produced by PyTealParser#testlist.
    def exitTestlist(self, ctx:PyTealParser.TestlistContext):
        pass


    # Enter a parse tree produced by PyTealParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:PyTealParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by PyTealParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:PyTealParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by PyTealParser#classdef.
    def enterClassdef(self, ctx:PyTealParser.ClassdefContext):
        pass

    # Exit a parse tree produced by PyTealParser#classdef.
    def exitClassdef(self, ctx:PyTealParser.ClassdefContext):
        pass


    # Enter a parse tree produced by PyTealParser#arglist.
    def enterArglist(self, ctx:PyTealParser.ArglistContext):
        pass

    # Exit a parse tree produced by PyTealParser#arglist.
    def exitArglist(self, ctx:PyTealParser.ArglistContext):
        pass


    # Enter a parse tree produced by PyTealParser#argument.
    def enterArgument(self, ctx:PyTealParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PyTealParser#argument.
    def exitArgument(self, ctx:PyTealParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PyTealParser#comp_iter.
    def enterComp_iter(self, ctx:PyTealParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by PyTealParser#comp_iter.
    def exitComp_iter(self, ctx:PyTealParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by PyTealParser#comp_for.
    def enterComp_for(self, ctx:PyTealParser.Comp_forContext):
        pass

    # Exit a parse tree produced by PyTealParser#comp_for.
    def exitComp_for(self, ctx:PyTealParser.Comp_forContext):
        pass


    # Enter a parse tree produced by PyTealParser#comp_if.
    def enterComp_if(self, ctx:PyTealParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by PyTealParser#comp_if.
    def exitComp_if(self, ctx:PyTealParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by PyTealParser#encoding_decl.
    def enterEncoding_decl(self, ctx:PyTealParser.Encoding_declContext):
        pass

    # Exit a parse tree produced by PyTealParser#encoding_decl.
    def exitEncoding_decl(self, ctx:PyTealParser.Encoding_declContext):
        pass


    # Enter a parse tree produced by PyTealParser#yield_expr.
    def enterYield_expr(self, ctx:PyTealParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by PyTealParser#yield_expr.
    def exitYield_expr(self, ctx:PyTealParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by PyTealParser#yield_arg.
    def enterYield_arg(self, ctx:PyTealParser.Yield_argContext):
        pass

    # Exit a parse tree produced by PyTealParser#yield_arg.
    def exitYield_arg(self, ctx:PyTealParser.Yield_argContext):
        pass


    # Enter a parse tree produced by PyTealParser#strings.
    def enterStrings(self, ctx:PyTealParser.StringsContext):
        pass

    # Exit a parse tree produced by PyTealParser#strings.
    def exitStrings(self, ctx:PyTealParser.StringsContext):
        pass



del PyTealParser