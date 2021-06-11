import syntax.syntax_utils as u
from syntax.syntax_exception import SyntaxException
from lexical.token_model import Token
from syntax.syntax_exception import SyntaxException

def expectIntDeclaration(s):
    s.box['token'] = s.box['scanner'].getNextToken()
    if (s.box['token'].text != 'int'):
        raise SyntaxException('type declaration for main identifier Expected', s.box['token'])

def expectMainDeclaration(s):
    s.box['token'] = s.box['scanner'].getNextToken()
    if (s.box['token'].text != 'main'):
        raise SyntaxException('main identifier Expected', s.box['token'])

def expectOpeningCurlyBracket(s):
    s.box['token'] = s.box['scanner'].getNextToken()
    if (s.box['token'].text != '{'):
        raise SyntaxException('opening curly braces Expected', s.box['token'])

def expectNumberOrIdentifier(s):
    if (s.box['token'].type != Token.TK_IDENTIFIER and s.box['token'].type != Token.TK_INT and s.box['token'].type != Token.TK_FLOAT and s.box['token'].type != Token.TK_CHAR):
        raise SyntaxException('identifier or number Expected', s.box['token'])

def expectArithmeticOperator(s):
    if (s.box['token'].type != Token.TK_ARITHMETIC_OPERATOR):
        raise SyntaxException('operator Expected', s.box['token'])

def expectVariableTypeDeclaration(s):
    if (not (s.box['token'].text == 'int' or s.box['token'].text == 'float' 
            or s.box['token'].text == 'char' or s.box['token'].type == Token.TK_IDENTIFIER)):
        raise SyntaxException('type Declaration Expected', s.box['token'])

def expectNextAttrOperatorOrSemicolonOrComma(s):
    s.box['token'] = s.box['scanner'].getNextToken()
    if (not u.isAttributionOperator(s.box['token'].text) and not u.isComma(s.box['token'].text) and not u.isSemicolon(s.box['token'].text)):
        raise SyntaxException('attribution operator, semicolon or comma Expected', s.box['token'])

def expectSemicolonOrComma(s):
    if (not u.isComma(s.box['token'].text) and not u.isSemicolon(s.box['token'].text)):
        raise SyntaxException('semicolon or comma Expected', s.box['token'])

def expectRelationalOperator(s):
    if (s.box['token'].type != Token.TK_RELATIONAL_OPERATOR):
        raise SyntaxException('relational operator Expected', s.box['token'])

def expectOpeningParenthesis(s):
    s.box['token'] = s.box['scanner'].getNextToken()
    if (s.box['token'].text != '('):
        raise SyntaxException('opening Parenthesis Expected', s.box['token'])

def expectClosingParenthesis(s):
    if (s.box['token'].text != ')'):
        raise SyntaxException('closing Parenthesis Expected', s.box['token'])