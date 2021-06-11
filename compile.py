import sys
import datetime
from utils.logger import log
from lexical.lexical_analysis import LexicalAnalysis 
from syntax.syntax_analysis import SyntaxAnalysis 
from semantic.semantic_analysis import SemanticAnalysis

class Compile:

    def __init__(self, code_name = '', code_content = '', testing = False):
        begin_time = datetime.datetime.now()

        if (not code_content):
            (code_name, code_content) = self.readCode()

        log('Compiling...', (255, 250, 205), testing)

        la = LexicalAnalysis(code_content)
        sema = SemanticAnalysis()
        syna = SyntaxAnalysis(la, sema)

        try:
            syna.execute()
            execution_time = datetime.datetime.now() - begin_time
            log('Successfully Compiled in ' + str(execution_time), (0, 255, 0), testing)
        except Exception as e:
            if (testing):
                raise e
            else:
                log(e, (255, 0, 0), testing)

        if (not testing):
            sema.outputSymbolTable(code_name)
            la.outputLexicalTokens(code_name)

    def readCode(self):
        code = ''
        code_name = 'code.c'
        try:
            code_name = sys.argv[1]
            code = open(code_name, "r").read()
        except Exception as e:
            code = open(code_name, "r").read()
        return [code_name, list(code)]

def main():
    Compile()
    
if (__name__ == '__main__'):
    main()