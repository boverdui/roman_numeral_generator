class RomanNumeralGenerator(object):

  POWERS_OF_TEN = ['M', 'C', 'X', 'I']

  GROUPS_OF_FIVE = [
    ('CCCCC', 'D'),
    ('XXXXX', 'L'),
    ('IIIII', 'V')
  ]

  SUBTRACTIVE_NOTATION = [
    ('DCCCC', 'CM'),
    ('CCCC', 'CD'),
    ('LXXXX', 'XC'),
    ('XXXX', 'XL'),
    ('VIIII', 'IX'),
    ('IIII', 'IV')
  ]

  def generate(self, number):

    if type(number) != int:
      raise TypeError('Number should be an integer')
    if number < 1 or number > 3999:
      raise ValueError('Number should be between 1 and 3999')

    result = ''

    i=1
    while i < len(str(number)) + 1:
      result = self.POWERS_OF_TEN[-i] * int(str(number)[-i]) + result
      i+=1

    for group_of_five, abbreviation in self.GROUPS_OF_FIVE:
      result = result.replace(group_of_five, abbreviation)

    for nonsubtractive, subtractive in self.SUBTRACTIVE_NOTATION:
      result = result.replace(nonsubtractive, subtractive)

    return result
