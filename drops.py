def drops(num: int) -> str:
  factors = [
    num % 3 == 0,
    num % 5 == 0,
    num % 7 == 0
  ]

  if not True in factors:
    return str(num)
  else:
    return getSounds(factors)

def getSounds(factors: list) -> str:
  sound = ''
  if factors[0]:
    sound += 'Plic'
  if factors[1]:
    sound += 'Plac'
  if factors[2]:
    sound += 'Ploc'
  return sound

if __name__ == '__main__':
  print(drops(28))
  print(drops(30))
  print(drops(34))