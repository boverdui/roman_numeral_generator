class RomanNumeralGenerator(object):

  ABBREVIATIONS = [
    ('IIIII', 'V'),
    ('VV', 'X'),
    ('XXXXX', 'L'),
    ('LL', 'C'),
    ('CCCCC', 'D'),
    ('DD', 'M'),
    ('IIII', 'IV'),
    ('VIV', 'IX'),
    ('XXXX', 'XL'),
    ('LXL', 'XC'),
    ('CCCC', 'CD'),
    ('DCD', 'CM')
  ]

  def generate(self, number):

    if type(number) != int:
      raise TypeError('Number should be an integer')
    if number < 1 or number > 3999:
      raise ValueError('Number should be between 1 and 3999')

    result = 'I' * number

    for numeral, abbreviation in self.ABBREVIATIONS:
        result = result.replace(numeral, abbreviation)

    return result
