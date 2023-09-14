parser grammar PyTealParser;

options {
    superClass = PyTealParserBase;
    tokenVocab = PyTealLexer;
}

file_input
    : (NEWLINE | stmt)* EOF
    ;

single_input
    : NEWLINE
    | simple_stmts
    | compound_stmt NEWLINE
    ;
  
eval_input
    : testlist NEWLINE* EOF
    ;

decorator
    : '@' dotted_name ( '(' arglist? ')' )? NEWLINE
    ;
  
decorators
    : decorator+
    ;
  
decorated
    : decorators (classdef | funcdef | async_funcdef)
    ;

async_funcdef
    : ASYNC funcdef
    ;
  
funcdef
    : 'def' name parameters ('->' test)? ':' block
    ;

parameters
    : '(' typedargslist? ')'
    ;
  
typedargslist
    : (tfpdef ('=' test)? (',' tfpdef ('=' test)?)* (',' ( '*' tfpdef? (',' tfpdef ('=' test)?)* (',' ('**' tfpdef ','? )? )?
    | '**' tfpdef ','? )? )?
    | '*' tfpdef? (',' tfpdef ('=' test)?)* (',' ('**' tfpdef ','? )? )?
    | '**' tfpdef ','?)
    ;
  
tfpdef
    : name (':' test)?
    ;
  
varargslist
    : (vfpdef ('=' test)? (',' vfpdef ('=' test)?)* (',' ( '*' vfpdef? (',' vfpdef ('=' test)?)* (',' ('**' vfpdef ','? )? )?
    | '**' vfpdef (',')?)?)?
    | '*' vfpdef? (',' vfpdef ('=' test)?)* (',' ('**' vfpdef ','? )? )?
    | '**' vfpdef ','? )
    ;
  
vfpdef
    : name
    ;

stmt
    : simple_stmts | compound_stmt
    ;
  
simple_stmts
    : simple_stmt (';' simple_stmt)* ';'? NEWLINE
    ;
  
simple_stmt
    : expr_stmt
    | del_stmt
    | pass_stmt
    | flow_stmt
    | import_stmt
    | global_stmt
    | nonlocal_stmt
    | assert_stmt
    ;
  
expr_stmt
    : testlist_star_expr (annassign | augassign (yield_expr|testlist) | ('=' (yield_expr|testlist_star_expr))*)
    ;
  
annassign
    : ':' test ('=' test)?
    ;
  
testlist_star_expr
    : (test|star_expr) (',' (test|star_expr))* ','?
    ;
  
augassign
    : ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=' | '**=' | '//=')
    ;

del_stmt
    : 'del' exprlist
    ;
  
pass_stmt
    : 'pass'
    ;
  
flow_stmt
    : break_stmt
    | continue_stmt
    | return_stmt
    | raise_stmt
    | yield_stmt
    ;
  
break_stmt
    : 'break'
    ;
  
continue_stmt
    : 'continue'
    ;
  
return_stmt
    : 'return' testlist?
    ;
  
yield_stmt
    : yield_expr
    ;
  
raise_stmt
    : 'raise' (test ('from' test)?)?
    ;
  
import_stmt
    : import_name | import_from
    ;
  
import_name
    : 'import' dotted_as_names
    ;

import_from
    : ('from' ((DOT | '...')* dotted_name | (DOT | '...')+ ) 'import' ('*' | '(' import_as_names ')' | import_as_names))
    ;
  
import_as_name
    : name ('as' name)?
    ;
  
dotted_as_name
    : dotted_name ('as' name)?
    ;
  
import_as_names
    : import_as_name (',' import_as_name)* ','?
    ;
  
dotted_as_names
    : dotted_as_name (',' dotted_as_name)*
    ;
  
dotted_name
    : name (DOT name)*
    ;
  
global_stmt
    : 'global' name (',' name)*
    ;
  
nonlocal_stmt
    : 'nonlocal' name (',' name)*
    ;
  
assert_stmt
    : 'assert' test (',' test)?
    ;

compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    | try_stmt
    | with_stmt
    | funcdef
    | classdef
    | decorated
    | async_stmt
    | match_stmt
    ;
  
async_stmt
    : ASYNC (funcdef | with_stmt | for_stmt)
    ;
  
if_stmt
    : 'if' test ':' block ('elif' test ':' block)* ('else' ':' block)?
    ;
  
while_stmt
    : 'while' test ':' block ('else' ':' block)?
    ;
  
for_stmt
    : 'for' exprlist 'in' testlist ':' block ('else' ':' block)?
    ;
  
try_stmt
    : ('try' ':' block
        ((except_clause ':' block)+
        ('else' ':' block)?
        ('finally' ':' block)? |
        'finally' ':' block))
    ;
  
with_stmt
    : 'with' with_item (',' with_item)*  ':' block
    ;
  
with_item
    : test ('as' expr)?
    ;

except_clause
    : 'except' (test ('as' name)?)?
    ;
  
block
    : simple_stmts
    | NEWLINE INDENT stmt+ DEDENT
    ;
  
match_stmt
    : 'match' subject_expr ':' NEWLINE INDENT case_block+ DEDENT 
    ;
  
subject_expr
    : star_named_expression ',' star_named_expressions?
    | test 
    ; 

star_named_expressions
    : ',' star_named_expression+ ','? 
    ;
  
star_named_expression
    : '*' expr
    | test 
    ;
  
case_block
    : 'case' patterns guard? ':' block 
    ;
  
guard
    : 'if' test
    ;
    
patterns
    : open_sequence_pattern
    | pattern
    ;
  
pattern
    : as_pattern
    | or_pattern 
    ;
  
as_pattern
    : or_pattern 'as' pattern_capture_target
    ;
  
or_pattern
    : closed_pattern ('|' closed_pattern)*
    ;
  
closed_pattern
    : literal_pattern
    | capture_pattern
    | wildcard_pattern
    | value_pattern
    | group_pattern
    | sequence_pattern
    | mapping_pattern
    | class_pattern
    ;
  
literal_pattern
    : signed_number { self.CannotBePlusMinus() }?
    | complex_number
    | strings
    | 'None'
    | 'True'
    | 'False'
    ;
  
literal_expr
    : signed_number { self.CannotBePlusMinus() }?
    | complex_number
    | strings
    | 'None'
    | 'True'
    | 'False'
    ;
  
complex_number
    : signed_real_number '+' imaginary_number 
    | signed_real_number '-' imaginary_number  
    ;
  
signed_number
    : NUMBER
    | '-' NUMBER
    ;
  
signed_real_number
    : real_number
    | '-' real_number
    ;
    
real_number
    : NUMBER
    ;
  
imaginary_number
    : NUMBER
    ;
  
capture_pattern
    : pattern_capture_target
    ;
  
pattern_capture_target
    : /* cannot be '_' */ name { self.CannotBeDotLpEq() }?
    ;
  
wildcard_pattern
    : '_' 
    ;
  
value_pattern
    : attr { self.CannotBeDotLpEq() }?
    ;
  
attr
    : name (DOT name)+
    ;
  
name_or_attr
    : attr
    | name
    ;
  
group_pattern
    : '(' pattern ')'
    ;
  
sequence_pattern
    : '[' maybe_sequence_pattern? ']' 
    | '(' open_sequence_pattern? ')' 
    ;
  
open_sequence_pattern
    : maybe_star_pattern ',' maybe_sequence_pattern?
    ;
  
maybe_sequence_pattern
    : maybe_star_pattern (',' maybe_star_pattern)* ','?
    ;
  
maybe_star_pattern
    : star_pattern
    | pattern
    ;
  
star_pattern
    : '*' pattern_capture_target 
    | '*' wildcard_pattern 
    ;
  
mapping_pattern
    : '{' '}' 
    | '{' double_star_pattern ','? '}' 
    | '{' items_pattern ',' double_star_pattern ','? '}' 
    | '{' items_pattern ','? '}' 
    ;
  
items_pattern
    : key_value_pattern (',' key_value_pattern)*
    ;
  
key_value_pattern
    : (literal_expr | attr) ':' pattern
    ;
  
double_star_pattern
    : '**' pattern_capture_target
    ;
  
class_pattern
    : name_or_attr '(' ')' 
    | name_or_attr '(' positional_patterns ','? ')' 
    | name_or_attr '(' keyword_patterns ','? ')' 
    | name_or_attr '(' positional_patterns ',' keyword_patterns ','? ')' 
    ;
  
positional_patterns
    : pattern (',' pattern)*
    ;
  
keyword_patterns
    : keyword_pattern (',' keyword_pattern)*
    ;
  
keyword_pattern
    : name '=' pattern
    ;

test
    : or_test ('if' or_test 'else' test)?
    | lambdef
    ;
  
test_nocond
    : or_test
    | lambdef_nocond
    ;
  
lambdef
    : 'lambda' varargslist? ':' test
    ;
  
lambdef_nocond
    : 'lambda' varargslist? ':' test_nocond
    ;
    
or_test
    : and_test ('or' and_test)*
    | pyteal_or_expr
    | pyteal_bytes_or_expr
    ;
  
and_test
    : not_test ('and' not_test)*
    | pyteal_and_expr
    | pyteal_bytes_and_expr
    ;
  
not_test
    : 'not' not_test
    | pyteal_not_expr
    | pyteal_bytes_not_expr
    | comparison
    ;
  
comparison
    : expr (comp_op expr)*
    | pyteal_comparison
    | pyteal_bytes_comparison
    ;

comp_op
    : '<'
    | '>'
    | '==' 
    | '>='
    | '<='
    | '<>'
    | '!='
    | 'in'
    | 'not' 'in'
    | 'is'
    | 'is' 'not'
    ;

star_expr
    : '*' expr
    ;

expr
    : atom_expr
    | expr '**' expr
    | pyteal_exp_expr
    | ('+'|'-'|'~')+ expr
    | pyteal_bitwise_not_expr
    | expr ('*'|'@'|'/'|'%'|'//') expr
    | ( pyteal_mul_expr | pyteal_div_expr | pyteal_mod_expr )
    | ( pyteal_bytes_mul_expr | pyteal_bytes_div_expr | pyteal_bytes_mod_expr )
    | expr ('+'|'-') expr
    | ( pyteal_add_expr | pyteal_minus_expr )
    | ( pyteal_bytes_add_expr | pyteal_bytes_minus_expr )
    | expr ('<<' | '>>') expr
    | expr '&' expr
    | pyteal_bitwise_and_expr
    | expr '^' expr
    | pyteal_bitwise_xor_expr
    | pyteal_bytes_xor_expr
    | expr '|' expr
    | pyteal_bitwise_or_expr
    | pyteal_bytes_zero_expr
    ;


pyteal_data_expr
    : pyteal_integers_expr
    | pyteal_bytes_expr
    | pyteal_conversion_expr
    ;

pyteal_integers_expr
    : PYTEAL_INT OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_expr
    : PYTEAL_BYTE OPEN_PAREN ( pyteal_bytes_base COMMA )? test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_base
    : PYTEAL_BYTE_BASE16
    | PYTEAL_BYTE_BASE32
    | PYTEAL_BYTE_BASE64
    ;

pyteal_conversion_expr
    : ( PYTEAL_ITOB | PYTEAL_BTOI ) OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_arithmetic_operations
    : pyteal_comparison
    | pyteal_bytes_comparison
    | pyteal_or_expr
    | pyteal_and_expr
    | pyteal_not_expr
    | pyteal_exp_expr
    | pyteal_add_expr
    | pyteal_minus_expr
    | pyteal_bitwise_not_expr
    | pyteal_mul_expr
    | pyteal_div_expr
    | pyteal_mod_expr
    | pyteal_bitwise_and_expr
    | pyteal_bitwise_xor_expr
    | pyteal_bitwise_or_expr
    | pyteal_bytes_or_expr
    | pyteal_bytes_and_expr
    | pyteal_bytes_not_expr
    | pyteal_bytes_mul_expr
    | pyteal_bytes_div_expr
    | pyteal_bytes_mod_expr
    | pyteal_bytes_add_expr
    | pyteal_bytes_minus_expr
    | pyteal_bytes_xor_expr
    | pyteal_bytes_zero_expr
    ;

pyteal_comparison
    : pyteal_comp_op OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;
  
pyteal_comp_op
    : PYTEAL_LT
    | PYTEAL_GT
    | PYTEAL_EQ
    | PYTEAL_GE
    | PYTEAL_LE
    | PYTEAL_NEQ
    ;

pyteal_bytes_comparison
    : pyteal_bytes_comp_op OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_comp_op
    : PYTEAL_BYTES_LT
    | PYTEAL_BYTES_GT
    | PYTEAL_BYTES_EQ
    | PYTEAL_BYTES_GE
    | PYTEAL_BYTES_LE
    | PYTEAL_BYTES_NEQ
    ;
  
pyteal_or_expr
    : PYTEAL_OR OPEN_PAREN test ( COMMA test )* COMMA? CLOSE_PAREN
    ;

pyteal_and_expr
    : PYTEAL_AND OPEN_PAREN test ( COMMA test )* COMMA? CLOSE_PAREN
    ;

pyteal_not_expr
    : PYTEAL_NOT OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_exp_expr
    : PYTEAL_EXP OPEN_PAREN test COMMA? COMMA test CLOSE_PAREN
    ;

pyteal_add_expr
    : PYTEAL_ADD OPEN_PAREN test COMMA? COMMA test CLOSE_PAREN
    ;
  
pyteal_minus_expr
    : PYTEAL_MINUS OPEN_PAREN test COMMA? COMMA test CLOSE_PAREN
    ;
  
pyteal_bitwise_not_expr
    : PYTEAL_BITWISENOT OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_mul_expr
    : PYTEAL_MUL OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_div_expr
    : PYTEAL_DIV OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_mod_expr
    : PYTEAL_MOD OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bitwise_and_expr
    : PYTEAL_BITWISEAND OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bitwise_xor_expr
    : PYTEAL_BITWISEXOR OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bitwise_or_expr
    : PYTEAL_BITWISEOR OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_or_expr
    : PYTEAL_BYTES_OR OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_and_expr
    : PYTEAL_BYTES_AND OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_not_expr
    : PYTEAL_BYTES_NOT OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_mul_expr
    : PYTEAL_BYTES_MUL OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_div_expr
    : PYTEAL_BYTES_DIV OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_mod_expr
    : PYTEAL_BYTES_MOD OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ; 

pyteal_bytes_add_expr
    : PYTEAL_BYTES_ADD OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_minus_expr
    : PYTEAL_BYTES_MINUS OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_xor_expr
    : PYTEAL_BYTES_XOR OPEN_PAREN test COMMA test COMMA? CLOSE_PAREN
    ;

pyteal_bytes_zero_expr
    : PYTEAL_BYTES_ZERO OPEN_PAREN test COMMA? CLOSE_PAREN
    ;

pyteal_txn_expr
    // Common Fields
    : pyteal_txn_type_expr
    | pyteal_txn_type_enum_expr
    | pyteal_txn_sender_expr
    | pyteal_txn_fee_expr
    | pyteal_txn_first_valid_expr
    | pyteal_txn_first_valid_time_expr
    | pyteal_txn_last_valid_expr
    | pyteal_txn_note_expr
    | pyteal_txn_lease_expr
    | pyteal_txn_group_index_expr
    | pyteal_txn_tx_id_expr
    | pyteal_txn_rekey_to_expr
  
    // Application Call
    | pyteal_txn_application_id_expr
    | pyteal_txn_on_completion_expr
    | pyteal_txn_approval_program_expr
    | pyteal_txn_global_num_uints_expr
    | pyteal_txn_global_num_byte_slices_expr
    | pyteal_txn_local_num_uints_expr
    | pyteal_txn_local_num_byte_slices_expr
    | pyteal_txn_accounts_expr
    | pyteal_txn_assets_expr
    | pyteal_txn_applications_expr
    | pyteal_txn_clear_state_program_expr
    | pyteal_txn_extra_program_pages_expr
    | pyteal_txn_application_args_expr
    | pyteal_txn_created_application_id_expr
    | pyteal_txn_logs_expr
    | pyteal_txn_last_log_expr
    | pyteal_txn_approval_program_pages_expr
    | pyteal_txn_clear_state_program_pages_expr
    
    // Asset Config
    | pyteal_txn_config_asset_expr
    | pyteal_txn_config_asset_total_expr
    | pyteal_txn_config_asset_decimals_expr
    | pyteal_txn_config_asset_default_frozen_expr
    | pyteal_txn_config_asset_unit_name_expr
    | pyteal_txn_config_asset_name_expr
    | pyteal_txn_config_asset_url_expr
    | pyteal_txn_config_asset_metadata_hash_expr
    | pyteal_txn_config_asset_manager_expr
    | pyteal_txn_config_asset_reserve_expr
    | pyteal_txn_config_asset_freeze_expr
    | pyteal_txn_config_asset_clawback_expr
    | pyteal_txn_created_asset_id_expr
    
    // Asset Freeze
    | pyteal_txn_freeze_asset_expr
    | pyteal_txn_freeze_asset_account_expr
    | pyteal_txn_freeze_asset_frozen_expr
    
    // Asset Transfer
    | pyteal_txn_xfer_asset_expr
    | pyteal_txn_asset_amount_expr
    | pyteal_txn_asset_sender_expr
    | pyteal_txn_asset_receiver_expr
    | pyteal_txn_asset_close_to_expr
    
    // Key Registration
    | pyteal_txn_vote_pk_expr
    | pyteal_txn_selection_pk_expr
    | pyteal_txn_state_proof_pk_expr
    | pyteal_txn_vote_first_expr
    | pyteal_txn_vote_last_expr
    | pyteal_txn_vote_key_dilution_expr
    | pyteal_txn_nonparticipation_expr
    
    // Payment
    | pyteal_txn_receiver_expr
    | pyteal_txn_amount_expr
    | pyteal_txn_close_remainder_to_expr
    
    // Transaction Types
    | pyteal_txntype_Unknown_expr
    | pyteal_txntype_Payment_expr
    | pyteal_txntype_KeyRegistration_expr
    | pyteal_txntype_AssetConfig_expr
    | pyteal_txntype_AssetTransfer_expr
    | pyteal_txntype_AssetFreeze_expr
    | pyteal_txntype_ApplicationCall_expr
    
    // Global Parameters
    | pyteal_global_min_txn_fee_expr
    | pyteal_global_min_balance_expr
    | pyteal_global_max_txn_life_expr
    | pyteal_global_zero_address_expr
    | pyteal_global_group_size_expr
    | pyteal_global_logic_sig_version_expr
    | pyteal_global_round_expr
    | pyteal_global_latest_timestamp_expr
    | pyteal_global_current_application_id_expr
    | pyteal_global_creator_address_expr
    | pyteal_global_current_application_address_expr
    | pyteal_global_group_id_expr
        
    // OTHERS
    | PYTEAL_TXN trailer*
    ;

/*********Common Fields**********/

pyteal_txn_type_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_TYPE OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_type_enum_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_TYPE_ENUM OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_sender_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_SENDER OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_fee_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FEE OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_first_valid_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FIRST_VALID OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_first_valid_time_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FIRST_VALID_TIME OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_last_valid_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_LAST_VALID OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_note_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_NOTE OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_lease_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_LEASE OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_group_index_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_GROUP_INDEX OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_tx_id_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_TXN_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_rekey_to_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_REKEY_TO OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Application Call**********/

pyteal_txn_application_id_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_APPLICATION_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_on_completion_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ON_COMPLETION OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_approval_program_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_APPROVAL_PROGRAM OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_global_num_uints_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_GLOBAL_NUM_UINTS OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_global_num_byte_slices_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_GLOBAL_NUM_BYTE_SLICES OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_local_num_uints_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_GLOBAL_LOCAL_NUM_UINTS OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_local_num_byte_slices_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_LOCAL_NUM_BYTE_SLICES OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_accounts_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ACCOUNTS trailer*
    ;

pyteal_txn_assets_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ASSETS trailer*
    ;

pyteal_txn_applications_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_APPLICATIONS trailer*
    ;

pyteal_txn_clear_state_program_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CLEAR_STATE_PROGRAM OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_extra_program_pages_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_EXTRA_PROGRAM_PAGES OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_application_args_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_APPLICATION_ARGS trailer*
    ;

pyteal_txn_created_application_id_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CREATED_APPLICATION_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_logs_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_LOGS trailer*
    ;

pyteal_txn_last_log_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_LAST_LOG OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_approval_program_pages_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_APPROVAL_PROGRAM_PAGES OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_clear_state_program_pages_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CLEAR_STATE_PROGRAM_PAGES OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Asset Config**********/

pyteal_txn_config_asset_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET OPEN_PAREN CLOSE_PAREN trailer*
    ;

pyteal_txn_config_asset_total_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_TOTAL OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_decimals_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_DECIMALS OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_default_frozen_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_DEFAULT_FROZEN OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_unit_name_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_UNIT_NAME OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_name_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_NAME OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_url_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_URL OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_metadata_hash_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_METADATA_HASH OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_manager_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_MANAGER OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_reserve_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_RESERVE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_freeze_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_FREEZE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_config_asset_clawback_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CONFIG_ASSET_CLAWBACK OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_created_asset_id_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CREATED_ASSET_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Asset Freeze**********/

pyteal_txn_freeze_asset_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FREEZE_ASSET OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_freeze_asset_account_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FREEZE_ASSET_ACCOUNT OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_freeze_asset_frozen_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_FREEZE_ASSET_FROZEN OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Asset Transfer**********/
pyteal_txn_xfer_asset_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_XFER_ASSET OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_asset_amount_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ASSET_AMOUNT OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_asset_sender_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ASSET_SENDER OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_asset_receiver_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ASSET_RECEIVER OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_asset_close_to_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_ASSET_CLOSE_TO OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Key Registration**********/
pyteal_txn_vote_pk_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_VOTE_PK OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_selection_pk_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_SELECTION_PK OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_state_proof_pk_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_STATE_PROOF_PK trailer*
    ;
  
pyteal_txn_vote_first_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_VOTE_FIRST OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_vote_last_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_VOTE_LAST OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_vote_key_dilution_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_VOTE_KEY_DILUTION OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_nonparticipation_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_NONPARTICIPATION OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Payment**********/
pyteal_txn_receiver_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_RECEIVER OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_amount_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_AMOUNT OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_txn_close_remainder_to_expr
    : PYTEAL_TXN PYTEAL_DOT PYTEAL_TXN_CLOSE_REMAINDER_TO OPEN_PAREN CLOSE_PAREN trailer*
    ;

/*********Transaction Types**********/
pyteal_txntype_Unknown_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_UNKNOWN trailer*
    ;
  
pyteal_txntype_Payment_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_PAYMENT trailer*
    ;
  
pyteal_txntype_KeyRegistration_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_KEYREGISTRATION trailer*
    ;
  
pyteal_txntype_AssetConfig_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_ASSETCONFIG trailer*
    ;
  
pyteal_txntype_AssetTransfer_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_ASSETTRANSFER trailer*
    ;
  
pyteal_txntype_AssetFreeze_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_ASSETFREEZE trailer*
    ;
  
pyteal_txntype_ApplicationCall_expr
    : PYTEAL_TXNTYPE PYTEAL_DOT PYTEAL_TXNTYPE_APPLICATIONCALL trailer*
    ;

/*********Global Parameters**********/
pyteal_global_min_txn_fee_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_MIN_TXN_FEE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_min_balance_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_MIN_BALANCE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_max_txn_life_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_MAX_TXN_LIFE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_zero_address_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_ZERO_ADDRESS OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_group_size_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_GROUP_SIZE OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_logic_sig_version_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_LOGIC_SIG_VERSION OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_round_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_ROUND OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_latest_timestamp_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_LATEST_TIMESTAMP OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_current_application_id_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_CURRENT_APPLICATION_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_creator_address_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_CREATOR_ADDRESS OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_current_application_address_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_CURRENT_APPLICATION_ADDRESS OPEN_PAREN CLOSE_PAREN trailer*
    ;
  
pyteal_global_group_id_expr
    : PYTEAL_GLOBAL PYTEAL_DOT PYTEAL_GLOBAL_GROUP_ID OPEN_PAREN CLOSE_PAREN trailer*
    ;

atom_expr
    : AWAIT? atom trailer*
    | pyteal_txn_expr
    | pyteal_data_expr
    ;
  
atom
    : '(' (yield_expr | testlist_comp)? ')'
    | '[' testlist_comp? ']'
    | '{' dictorsetmaker? '}'
    | name
    | NUMBER
    | STRING+
    | '...' 
    | 'None'
    | 'True'
    | 'False' 
    ;
  
name
    : NAME
    | '_'
    | 'match'
    ;
    
testlist_comp
    : (test|star_expr) ( comp_for | (',' (test|star_expr))* ','? )
    ;
  
trailer
    : '(' arglist? ')'
    | '[' subscriptlist ']'
    | DOT ( pyteal_arithmetic_operations | name )
    ;
  
subscriptlist
    : subscript_ (',' subscript_)* ','?
    ;
  
subscript_
    : test
    | test? ':' test? sliceop?
    ;
  
sliceop
    : ':' test?
    ;
  
exprlist
    : (expr|star_expr) (',' (expr|star_expr))* ','?
    ;
    
testlist
    : test (',' test)* ','?
    ;
    
dictorsetmaker
    : ( ((test ':' test | '**' expr)
        (comp_for | (',' (test ':' test | '**' expr))* ','?)) |
        ((test | star_expr)
        (comp_for | (',' (test | star_expr))* ','?)) )
    ; 

classdef
    : 'class' name ('(' arglist? ')')? ':' block
    ;
  
arglist
    : argument (',' argument)* ','?
    ;

argument
    : ( test comp_for? |
        test '=' test |
        '**' test |
        '*' test )
    ;

comp_iter
    : comp_for
    | comp_if
    ;
    
comp_for
    : ASYNC? 'for' exprlist 'in' or_test comp_iter?
    ;
    
comp_if
    : 'if' test_nocond comp_iter?
    ;

encoding_decl
    : name
    ;

yield_expr
    : 'yield' yield_arg?
    ;
    
yield_arg
    : 'from' test
    | testlist
    ;

strings
    : STRING+ 
    ;
