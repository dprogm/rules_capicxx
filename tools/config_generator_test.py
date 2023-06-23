import unittest
import tools.config_generator as config_generator

class TestVariableSubstitution(unittest.TestCase):

  def test_single_substitution_with_defined_variable(self):
    var = {'VAR_X' : '123'}
    res_1 = config_generator.replace_variables('#define VAR_X ${VAR_X}', var)
    res_2 = config_generator.replace_variables('#define VAR_X @VAR_X@', var)
    res_3 = config_generator.replace_variables('#define VAR_X $ENV{VAR_X}', var)
    res_4 = config_generator.replace_variables('#define VAR_X $CACHE{VAR_X}', var)
    exp_sub = '#define VAR_X 123'
    self.assertEqual(res_1, exp_sub)
    self.assertEqual(res_2, exp_sub)
    self.assertEqual(res_3, exp_sub)
    self.assertEqual(res_4, exp_sub)

  def test_single_substitution_with_undefined_variable(self):
    var = {'VAR_Y' : '123'}
    res = config_generator.replace_variables('#define VAR_X ${VAR_X}', var)
    exp_sub = '#define VAR_X '
    self.assertEqual(res, exp_sub)

  def test_multiple_substitutions(self):
    var = {
      'VAR_X' : '123',
      'VAR_Y' : '456' }
    res = config_generator.replace_variables('#define VAR_X ${VAR_X} middle @VAR_Y@ end', var)
    exp_sub = '#define VAR_X 123 middle 456 end'
    self.assertEqual(res, exp_sub)

  def test_three_substitutions(self):
    var = {
      'VAR_X' : '123',
      'VAR_Y' : '456',
      'VAR_Z' : '789'  }
    input = '#define COMPLEX ((@VAR_X@ << 16) | (@VAR_Y@ << 8) | (@VAR_Z@)) '
    res = config_generator.replace_variables(input, var)
    exp_sub = '#define COMPLEX ((123 << 16) | (456 << 8) | (789)) '
    self.assertEqual(res, exp_sub)

if __name__ == '__main__':
    unittest.main()