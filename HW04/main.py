class Fraction:
  def __init__(
    self,
    numerator: int = 0,
    denominator: int = 1):
    if not isinstance(numerator, int) or not isinstance(denominator, int):
      raise TypeError("Numerator and denominator must be int")
    if denominator == 0:
      raise ValueError("Denominator cannot be zero")

    self.numerator = numerator
    self.denominator = denominator
    self._reduce()

  def __str__(self):
    return "%d / %d" % (self.numerator, self.denominator)

  def _gcd(
    self,
    a: int,
    b: int) -> int:
    while b != 0:
      a, b = b, a % b
    return abs(a)

  def _reduce(self):
    sign = -1 if self.numerator * self.denominator < 0 else 1
    a, b = abs(self.numerator), abs(self.denominator)
    d = self._gcd(a, b)
    self.numerator = sign * (a // d)
    self.denominator = b // d

  def to_float(self) -> float:
    return self.numerator / self.denominator

  def __add__(self, other):
    if not isinstance(other, Fraction):
      raise TypeError("Addition requires another Fraction")
    num = self.numerator * other.denominator + other.numerator * self.denominator
    den = self.denominator * other.denominator
    return Fraction(num, den)

  def __sub__(self, other):
    if not isinstance(other, Fraction):
      raise TypeError("Subtraction requires another Fraction")
    num = self.numerator * other.denominator - other.numerator * self.denominator
    den = self.denominator * other.denominator
    return Fraction(num, den)

  def __mul__(self, other):
    if not isinstance(other, Fraction):
      raise TypeError("Multiplication requires another Fraction")
    num = self.numerator * other.numerator
    den = self.denominator * other.denominator
    return Fraction(num, den)

  def __truediv__(self, other):
    if not isinstance(other, Fraction):
      raise TypeError("Division requires another Fraction")
    if other.numerator == 0:
      raise ZeroDivisionError("Division by zero fraction")
    num = self.numerator * other.denominator
    den = self.denominator * other.numerator
    return Fraction(num, den)


def main():
  f1 = Fraction(4, 6)
  f2 = Fraction(3, 9)
  print("f1 =", f1)
  print("f2 =", f2)

  print("f1 + f2 =", f1 + f2)
  print("f1 - f2 =", f1 - f2)
  print("f1 * f2 =", f1 * f2)
  print("f1 / f2 =", f1 / f2)

  print("As float:", f1.to_float())


if __name__ == "__main__":
  main()
