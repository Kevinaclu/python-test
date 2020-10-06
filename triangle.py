import math

class Triangle:
  def __init__(self, a: float, b: float, c: float):
    self.__a = a
    self.__b = b
    self.__c = c

  def getArea(self):
    p = self.__getSemiPerimetro()
    a = self.__a
    b = self.__b
    c = self.__c
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area

  def __getSemiPerimetro(self) -> float:
    return (self.__a + self.__b + self.__c) / 2


if __name__ == '__main__':
  t = Triangle(4,4,4)
  print(t.getArea())
  # print(t.__a)
  # print(t.__b)
  # print(t.__c)
  # print(t.__getSemiPerimetro())
