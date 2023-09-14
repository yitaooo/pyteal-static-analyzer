lexer grammar PyTealLexer;

tokens { INDENT, DEDENT }

options {
    superClass = PyTealLexerBase;
}

/*---------------------------------------------- lexer rules ------------------------------------------------*/

// PyTeal Keyword
PYTEAL_INT : 'Int' ;
PYTEAL_BYTE : 'Bytes' ;
PYTEAL_BYTE_BASE16 : '"base16"' ;
PYTEAL_BYTE_BASE32 : '"base32"' ;
PYTEAL_BYTE_BASE64 : '"base64"' ;
PYTEAL_ITOB : 'Itob' ;
PYTEAL_BTOI : 'Btoi' ;
PYTEAL_LT : 'Lt' ;
PYTEAL_GT : 'Gt' ;
PYTEAL_LE : 'Le' ;
PYTEAL_GE : 'Ge' ;
PYTEAL_ADD : 'Add' ;
PYTEAL_MINUS : 'Minus' ;
PYTEAL_MUL : 'Mul' ;
PYTEAL_DIV : 'Div' ;
PYTEAL_MOD : 'Mod' ;
PYTEAL_EXP : 'Exp' ;
PYTEAL_EQ : 'Eq' ;
PYTEAL_NEQ : 'Neq' ;
PYTEAL_AND : 'And' ;
PYTEAL_OR : 'Or' ;
PYTEAL_NOT : 'Not' ;
PYTEAL_BITWISEAND : 'BitwiseAnd' ;
PYTEAL_BITWISEOR : 'BitwiseOr' ;
PYTEAL_BITWISEXOR : 'BitwiseXor' ;
PYTEAL_BITWISENOT : 'BitwiseNot' ;

PYTEAL_BYTES_LT : 'BytesLt' ;
PYTEAL_BYTES_GT : 'BytesGt' ;
PYTEAL_BYTES_LE : 'BytesLe' ;
PYTEAL_BYTES_GE : 'BytesGe' ;
PYTEAL_BYTES_ADD : 'BytesAdd' ;
PYTEAL_BYTES_MINUS : 'BytesMinus' ;
PYTEAL_BYTES_MUL : 'BytesMul' ;
PYTEAL_BYTES_DIV : 'BytesDiv' ;
PYTEAL_BYTES_MOD : 'BytesMod' ;
PYTEAL_BYTES_EQ : 'BytesEq' ;
PYTEAL_BYTES_NEQ : 'BytesNeq' ;
PYTEAL_BYTES_AND : 'BytesAnd' ;
PYTEAL_BYTES_OR : 'BytesOr' ;
PYTEAL_BYTES_NOT : 'BytesNot' ;
PYTEAL_BYTES_XOR : 'BytesXor' ;
PYTEAL_BYTES_ZERO : 'BytesZero' ;

PYTEAL_TXN : 'Txn' -> pushMode(PYTEAL_TXN_MODE) ;
PYTEAL_INNERTXN : 'InnerTxn' -> pushMode(PYTEAL_TXN_MODE) ;
PYTEAL_TXNTYPE : 'TxnType' -> pushMode(PYTEAL_TXN_MODE) ;
PYTEAL_GLOBAL : 'Global' -> pushMode(PYTEAL_TXN_MODE) ;

// keyword
AND : 'and';
AS : 'as';
ASSERT : 'assert';
ASYNC : 'async';
AWAIT : 'await';
BREAK : 'break';
CASE : 'case' ;
CLASS : 'class';
CONTINUE : 'continue';
DEF : 'def';
DEL : 'del';
ELIF : 'elif';
ELSE : 'else';
EXCEPT : 'except';
FALSE : 'False';
FINALLY : 'finally';
FOR : 'for';
FROM : 'from';
GLOBAL : 'global';
IF : 'if';
IMPORT : 'import';
IN : 'in';
IS : 'is';
LAMBDA : 'lambda';
MATCH : 'match' ;
NONE : 'None';
NONLOCAL : 'nonlocal';
NOT : 'not';
OR : 'or';
PASS : 'pass';
RAISE : 'raise';
RETURN : 'return';
TRUE : 'True';
TRY : 'try';
UNDERSCORE : '_' ;
WHILE : 'while';
WITH : 'with';
YIELD : 'yield';

// operator
DOT : '.';
ELLIPSIS : '...';
STAR : '*';
OPEN_PAREN : '(' {self.openBrace();};
CLOSE_PAREN : ')' {self.closeBrace();};
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';
POWER : '**';
ASSIGN : '=';
OPEN_BRACK : '[' {self.openBrace();};
CLOSE_BRACK : ']' {self.closeBrace();};
OR_OP : '|';
XOR : '^';
AND_OP : '&';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
IDIV : '//';
NOT_OP : '~';
OPEN_BRACE : '{' {self.openBrace();};
CLOSE_BRACE : '}' {self.closeBrace();};
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ_1 : '<>';
NOT_EQ_2 : '!=';
AT : '@';
ARROW : '->';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
AT_ASSIGN : '@=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
POWER_ASSIGN : '**=';
IDIV_ASSIGN : '//=';

STRING
 : STRING_LITERAL
 | BYTES_LITERAL
 ;

NUMBER
 : INTEGER
 | FLOAT_NUMBER
 | IMAG_NUMBER
 ;

INTEGER
 : DECIMAL_INTEGER
 | OCT_INTEGER
 | HEX_INTEGER
 | BIN_INTEGER
 ;

NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
   {self.onNewLine();}
 ;

NAME
 : ID_START ID_CONTINUE*
 ;

STRING_LITERAL
 : ( [rR] | [uU] | [fF] | ( [fF] [rR] ) | ( [rR] [fF] ) )? ( SHORT_STRING | LONG_STRING )
 ;

BYTES_LITERAL
 : ( [bB] | ( [bB] [rR] ) | ( [rR] [bB] ) ) ( SHORT_BYTES | LONG_BYTES )
 ;

DECIMAL_INTEGER
 : NON_ZERO_DIGIT DIGIT*
 | '0'+
 ;

OCT_INTEGER
 : '0' [oO] OCT_DIGIT+
 ;

HEX_INTEGER
 : '0' [xX] HEX_DIGIT+
 ;

BIN_INTEGER
 : '0' [bB] BIN_DIGIT+
 ;

FLOAT_NUMBER
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;

IMAG_NUMBER
 : ( FLOAT_NUMBER | INT_PART ) [jJ]
 ;

SKIP_
 : ( SPACES | COMMENT | LINE_JOINING ) -> skip
 ;

UNKNOWN_CHAR
 : .
 ;

fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
 ;

fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

fragment LONG_STRING_CHAR
 : ~'\\'
 ;

fragment STRING_ESCAPE_SEQ
 : '\\' .
 | '\\' NEWLINE
 ;

fragment NON_ZERO_DIGIT
 : [1-9]
 ;

fragment DIGIT
 : [0-9]
 ;

fragment OCT_DIGIT
 : [0-7]
 ;

fragment HEX_DIGIT
 : [0-9a-fA-F]
 ;

fragment BIN_DIGIT
 : [01]
 ;

fragment POINT_FLOAT
 : INT_PART? FRACTION
 | INT_PART '.'
 ;

fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;

fragment INT_PART
 : DIGIT+
 ;

fragment FRACTION
 : '.' DIGIT+
 ;

fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;

fragment SHORT_BYTES
 : '\'' ( SHORT_BYTES_CHAR_NO_SINGLE_QUOTE | BYTES_ESCAPE_SEQ )* '\''
 | '"' ( SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE | BYTES_ESCAPE_SEQ )* '"'
 ;

fragment LONG_BYTES
 : '\'\'\'' LONG_BYTES_ITEM*? '\'\'\''
 | '"""' LONG_BYTES_ITEM*? '"""'
 ;

fragment LONG_BYTES_ITEM
 : LONG_BYTES_CHAR
 | BYTES_ESCAPE_SEQ
 ;

fragment SHORT_BYTES_CHAR_NO_SINGLE_QUOTE
 : [\u0000-\u0009]
 | [\u000B-\u000C]
 | [\u000E-\u0026]
 | [\u0028-\u005B]
 | [\u005D-\u007F]
 ;

fragment SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE
 : [\u0000-\u0009]
 | [\u000B-\u000C]
 | [\u000E-\u0021]
 | [\u0023-\u005B]
 | [\u005D-\u007F]
 ;

fragment LONG_BYTES_CHAR
 : [\u0000-\u005B]
 | [\u005D-\u007F]
 ;

fragment BYTES_ESCAPE_SEQ
 : '\\' [\u0000-\u007F]
 ;

fragment SPACES
 : [ \t]+
 ;

fragment COMMENT
 : '#' ~[\r\n\f]*
 ;

fragment LINE_JOINING
 : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f')
 ;

fragment UNICODE_OIDS
 : '\u1885'..'\u1886'
 | '\u2118'
 | '\u212e'
 | '\u309b'..'\u309c'
 ;

fragment UNICODE_OIDC
 : '\u00b7'
 | '\u0387'
 | '\u1369'..'\u1371'
 | '\u19da'
 ;

fragment ID_START
 : '_'
 | [\p{L}]
 | [\p{Nl}]
 | UNICODE_OIDS
 ;

fragment ID_CONTINUE
 : ID_START
 | [\p{Mn}]
 | [\p{Mc}]
 | [\p{Nd}]
 | [\p{Pc}]
 | UNICODE_OIDC
 ;

/******************************* mode PYTEAL_TXN_MODE BEGIN **********************************************/
mode PYTEAL_TXN_MODE;
PYTEAL_DOT : '.';

/*********Common Fields**********/
PYTEAL_TXN_TYPE : 'type' -> popMode ;
PYTEAL_TXN_TYPE_ENUM : 'type_enum' -> popMode ;
PYTEAL_TXN_SENDER : 'sender' -> popMode ;
PYTEAL_TXN_FEE : 'fee' -> popMode ;
PYTEAL_TXN_FIRST_VALID : 'first_valid' -> popMode ;
PYTEAL_TXN_FIRST_VALID_TIME : 'first_valid_time' -> popMode ;
PYTEAL_TXN_LAST_VALID : 'last_valid' -> popMode ;
PYTEAL_TXN_NOTE : 'note' -> popMode ;
PYTEAL_TXN_LEASE : 'lease' -> popMode ;
PYTEAL_TXN_GROUP_INDEX : 'group_index' -> popMode ;
PYTEAL_TXN_TXN_ID : 'tx_id' -> popMode ;
PYTEAL_TXN_REKEY_TO : 'rekey_to' -> popMode ;

/*********Application Call**********/
PYTEAL_TXN_APPLICATION_ID : 'application_id' -> popMode ;
PYTEAL_TXN_ON_COMPLETION : 'on_completion' -> popMode ;
PYTEAL_TXN_APPROVAL_PROGRAM : 'approval_program' -> popMode ;
PYTEAL_TXN_GLOBAL_NUM_UINTS : 'global_num_uints' -> popMode ;
PYTEAL_TXN_GLOBAL_NUM_BYTE_SLICES : 'global_num_byte_slices' -> popMode ;
PYTEAL_TXN_GLOBAL_LOCAL_NUM_UINTS : 'local_num_uints' -> popMode ;
PYTEAL_TXN_LOCAL_NUM_BYTE_SLICES : 'local_num_byte_slices' -> popMode ;
PYTEAL_TXN_ACCOUNTS : 'accounts' -> popMode ;
PYTEAL_TXN_ASSETS : 'assets' -> popMode ;
PYTEAL_TXN_APPLICATIONS : 'applications' -> popMode ;
PYTEAL_TXN_CLEAR_STATE_PROGRAM : 'clear_state_program' -> popMode ;
PYTEAL_TXN_EXTRA_PROGRAM_PAGES : 'extra_program_pages' -> popMode ;
PYTEAL_TXN_APPLICATION_ARGS : 'application_args' -> popMode ;
PYTEAL_TXN_CREATED_APPLICATION_ID : 'created_application_id' -> popMode ;
PYTEAL_TXN_LOGS : 'logs' -> popMode ;
PYTEAL_TXN_LAST_LOG : 'last_log' -> popMode ;
PYTEAL_TXN_APPROVAL_PROGRAM_PAGES : 'approval_program_pages' -> popMode ;
PYTEAL_TXN_CLEAR_STATE_PROGRAM_PAGES : 'clear_state_program_pages' -> popMode ;

/*********Asset Config**********/
PYTEAL_TXN_CONFIG_ASSET : 'config_asset' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_TOTAL : 'config_asset_total' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_DECIMALS : 'config_asset_decimals' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_DEFAULT_FROZEN : 'config_asset_default_frozen' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_UNIT_NAME : 'config_asset_unit_name' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_NAME : 'config_asset_name' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_URL : 'config_asset_url' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_METADATA_HASH : 'config_asset_metadata_hash' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_MANAGER : 'config_asset_manager' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_RESERVE : 'config_asset_reserve' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_FREEZE : 'config_asset_freeze' -> popMode ;
PYTEAL_TXN_CONFIG_ASSET_CLAWBACK : 'config_asset_clawback' -> popMode ;
PYTEAL_TXN_CREATED_ASSET_ID : 'created_asset_id' -> popMode ;

/*********Asset Freeze**********/
PYTEAL_TXN_FREEZE_ASSET : 'freeze_asset' -> popMode ;
PYTEAL_TXN_FREEZE_ASSET_ACCOUNT : 'freeze_asset_account' -> popMode ;
PYTEAL_TXN_FREEZE_ASSET_FROZEN : 'freeze_asset_frozen' -> popMode ;

/*********Asset Transfer**********/
PYTEAL_TXN_XFER_ASSET : 'xfer_asset' -> popMode ;
PYTEAL_TXN_ASSET_AMOUNT : 'asset_amount' -> popMode ;
PYTEAL_TXN_ASSET_SENDER : 'asset_sender' -> popMode ;
PYTEAL_TXN_ASSET_RECEIVER : 'asset_receiver' -> popMode ;
PYTEAL_TXN_ASSET_CLOSE_TO : 'asset_close_to' -> popMode ;

/*********Key Registration**********/
PYTEAL_TXN_VOTE_PK : 'vote_pk' -> popMode ;
PYTEAL_TXN_SELECTION_PK : 'selection_pk' -> popMode ;
PYTEAL_TXN_STATE_PROOF_PK : 'state_proof_pk' -> popMode ;
PYTEAL_TXN_VOTE_FIRST : 'vote_first' -> popMode ;
PYTEAL_TXN_VOTE_LAST : 'vote_last' -> popMode ;
PYTEAL_TXN_VOTE_KEY_DILUTION : 'vote_key_dilution' -> popMode ;
PYTEAL_TXN_NONPARTICIPATION : 'nonparticipation' -> popMode ;

/*********Payment**********/
PYTEAL_TXN_RECEIVER : 'receiver' -> popMode ;
PYTEAL_TXN_AMOUNT : 'amount' -> popMode ;
PYTEAL_TXN_CLOSE_REMAINDER_TO : 'close_remainder_to' -> popMode ;

/*********Transaction Types**********/
PYTEAL_TXNTYPE_UNKNOWN : 'Unknown' -> popMode ;
PYTEAL_TXNTYPE_PAYMENT : 'Payment' -> popMode ;
PYTEAL_TXNTYPE_KEYREGISTRATION : 'KeyRegistration' -> popMode ;
PYTEAL_TXNTYPE_ASSETCONFIG : 'AssetConfig' -> popMode ;
PYTEAL_TXNTYPE_ASSETTRANSFER : 'AssetTransfer' -> popMode ;
PYTEAL_TXNTYPE_ASSETFREEZE : 'AssetFreeze' -> popMode ;
PYTEAL_TXNTYPE_APPLICATIONCALL : 'ApplicationCall' -> popMode ;

/*********Global Parameters**********/
PYTEAL_GLOBAL_MIN_TXN_FEE : 'min_txn_fee' -> popMode ;
PYTEAL_GLOBAL_MIN_BALANCE : 'min_balance' -> popMode ;
PYTEAL_GLOBAL_MAX_TXN_LIFE : 'max_txn_life' -> popMode ;
PYTEAL_GLOBAL_ZERO_ADDRESS : 'zero_address' -> popMode ;
PYTEAL_GLOBAL_GROUP_SIZE : 'group_size' -> popMode ;
PYTEAL_GLOBAL_LOGIC_SIG_VERSION : 'logic_sig_version' -> popMode ;
PYTEAL_GLOBAL_ROUND : 'round' -> popMode ;
PYTEAL_GLOBAL_LATEST_TIMESTAMP : 'latest_timestamp' -> popMode ;
PYTEAL_GLOBAL_CURRENT_APPLICATION_ID : 'current_application_id' -> popMode ;
PYTEAL_GLOBAL_CREATOR_ADDRESS : 'creator_address' -> popMode ;
PYTEAL_GLOBAL_CURRENT_APPLICATION_ADDRESS : 'current_application_address' -> popMode ;
PYTEAL_GLOBAL_GROUP_ID : 'group_id' -> popMode ;


/******************************* mode PYTEAL_TXN_MODE END **********************************************/
