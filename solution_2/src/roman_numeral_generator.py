class RomanNumeralGenerator(object):

  SYMBOLS = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
  ]

  def generate(self, number):

    if type(number) != int:
      raise TypeError('Number should be an integer')
    if number < 1 or number > 3999:
      raise ValueError('Number should be between 1 and 3999')

    result = ''

    for arabic, roman in self.SYMBOLS:
      while number >= arabic:
        result += roman
        number -= arabic

    return result
