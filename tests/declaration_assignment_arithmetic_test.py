from compile import Compile
from syntax.syntax_analysis import SyntaxAnalysis
from lexical.lexical_analysis import LexicalAnalysis
import unittest

class DeclarationAssingmentArithmeticTests(unittest.TestCase):

    def test_should_pass_all_declaration_assignment_arithmetic_cases(self):
        code_content = list("""
            int main() {

                int a = 1, b = 1, c = 1;

                a = 5;

                int d = 1, e = 1, f = 5;
                
                int g = 1, h, i;

                int j, k, l;

                float m = 1.5, n = 1;

                char o = 'a';

                a = 1, b = 1, c = 1;

                int z = 1;

                d = 1, e = 1, f;
                
                g = 1, h, i;

                o = 'a';

                a = ((1) + (1) - ((1 - 1) * 1));

                b = ((1 + a) + (1 + a) - ((1 - (a - 1)) * 1));

                d = (5 + 5 + (a * b)) / 2;

            }
        """)

        error = ''

        try:
            Compile(code_content=code_content, testing=True)
        except Exception as e:
            error = e.__str__()

        self.assertEqual(error, '')


if __name__ == '__main__':
    unittest.main()