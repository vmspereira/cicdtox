import unittest

class TestGPR(unittest.TestCase):
    """ Tests
    """

    def setUp(self):
        """Set up
        """
        pass


    def test_aritmetic(self):
        """Test aritmetic expression"""
        from parsing import Arithmetic, build_tree, ArithmeticEvaluator
        expression = " 1 + 2 + 3 + ( 2 * 2 )"
        t = build_tree(expression, Arithmetic)
        res = t.evaluate(ArithmeticEvaluator.f_operand, ArithmeticEvaluator.f_operator)
        self.assertEqual(res,10)
    
    def test_gpr(self):
        """Tests gpr
        """
        from parsing import Boolean, build_tree, BooleanEvaluator
        expression = "( (Lrp AND NOT (leu_L_e_>0)) OR NOT(((GlnG AND GlnB AND GlnD) AND RpoN) AND ((glu_L_e_>0) OR \
                       (arg_L_e_>0) OR (asp_L_e_>0) OR (his_L_e_>0) OR (pro_L_e_>0) )))"
        t = build_tree(expression, Boolean)
        true_list = ['GlnG']
        # dict of variables values
        v = {'leu_L_e_': 1, 'glu_L_e_': 7, "arg_L_e_": 0.5,
             "asp_L_e_": 2, "his_L_e_": 0, "pro_L_e_": 0}
        evaluator = BooleanEvaluator(true_list, v)
        res = t.evaluate(evaluator.f_operand, evaluator.f_operator)
        self.assertEqual(res, True)


    def test_ou(self):
        """
        Example on how to evaluate the over/under expression of genes using a GPR
        """
        from parsing import GeneEvaluator, Boolean, build_tree
        # Gene OU example
        gpr = "((G_YIL043C and G_YMR015C and G_YNL111C) or (G_YKL150W and G_YMR015C and G_YNL111C))"
        genes = {'G_YER091C': 0, 'G_YMR105C': 0.03125, 'G_YNL117W': 0.5, 'G_YNL111C': 0.125, 'G_YJR158W': 0.0625,
                'G_YLR355C': 0.5}
        operators = (lambda x, y: min(x, y), lambda x, y: max(x, y))
        evaluator = GeneEvaluator(genes, operators[0], operators[1])
        tree = build_tree(gpr, Boolean)
        lv = tree.evaluate(evaluator.f_operand, evaluator.f_operator)
        self.assertEqual(lv, 0.125)
        