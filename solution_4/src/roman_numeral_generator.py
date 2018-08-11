class RomanNumeralGenerator(object):

  SYMBOLS = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

  def generate(self, number):

    if type(number) != int:
      raise TypeError('Number should be an integer')
    if number < 1 or number > 3999:
      raise ValueError('Number should be between 1 and 3999')

    result = ''

    i = 1
    j = 1
    while i < len(str(number)) + 1:
      result = self.SYMBOLS[-j] * int(str(number)[-i]) + result
      i += 1
      j += 2

    i = 2
    while i < len(self.SYMBOLS):
      if (self.SYMBOLS[i] * 5) in result:
        result = result.replace(self.SYMBOLS[i] * 5, self.SYMBOLS[i-1])
      if (self.SYMBOLS[i-1] + self.SYMBOLS[i] * 4) in result:
        result = result.replace(self.SYMBOLS[i-1] + self.SYMBOLS[i] * 4, self.SYMBOLS[i] + self.SYMBOLS[i-2])
      if (self.SYMBOLS[i] * 4) in result:
        result = result.replace(self.SYMBOLS[i] * 4, self.SYMBOLS[i] + self.SYMBOLS[i-1])
      i += 2

    return result
