import unittest
from src.roman_numeral_generator import RomanNumeralGenerator

class RomanNumeralGeneratorTest(unittest.TestCase):

  def setUp(self):
    self.my_generator = RomanNumeralGenerator()

  def test_number_is_an_integer(self):
    self.assertRaises(TypeError, self.my_generator.generate, 0.1)
    self.assertRaises(TypeError, self.my_generator.generate, '1')

  def test_number_is_between_1_and_3999(self):
    self.assertRaises(ValueError, self.my_generator.generate, -1)
    self.assertRaises(ValueError, self.my_generator.generate, 0)
    self.assertRaises(ValueError, self.my_generator.generate, 4000)

  def test_basic_symbols(self):
    self.assertEqual('I', self.my_generator.generate(1))
    self.assertEqual('V', self.my_generator.generate(5))
    self.assertEqual('X', self.my_generator.generate(10))
    self.assertEqual('L', self.my_generator.generate(50))
    self.assertEqual('C', self.my_generator.generate(100))
    self.assertEqual('D', self.my_generator.generate(500))
    self.assertEqual('M', self.my_generator.generate(1000))

  def test_additive_notation(self):
    self.assertEqual('II', self.my_generator.generate(2))
    self.assertEqual('III', self.my_generator.generate(3))
    self.assertEqual('VI', self.my_generator.generate(6))
    self.assertEqual('XV', self.my_generator.generate(15))

  def test_subtractive_notation(self):
    self.assertEqual('IV', self.my_generator.generate(4))
    self.assertEqual('IX', self.my_generator.generate(9))
    self.assertEqual('XL', self.my_generator.generate(40))
    self.assertEqual('XC', self.my_generator.generate(90))
    self.assertEqual('CD', self.my_generator.generate(400))
    self.assertEqual('CM', self.my_generator.generate(900))

  def test_complex_numbers(self):
    self.assertEqual('MDCCLXXVI', self.my_generator.generate(1776))
    self.assertEqual('MCMLIV', self.my_generator.generate(1954))
    self.assertEqual('MCMXC', self.my_generator.generate(1990))
    self.assertEqual('MMXVIII', self.my_generator.generate(2018))
    self.assertEqual('MMMCMXCIX', self.my_generator.generate(3999))

if __name__ == '__main__':
    unittest.main()
