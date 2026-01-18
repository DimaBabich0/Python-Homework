from DataAccessor import DataAccessor


class Program:
  def __init__(self):
    try:
      self.data_accessor = DataAccessor()
    except RuntimeError as err:
      print(err)
      return

  def TestPBKDF2(self):
    self.data_accessor._test_pbkdf2()


def main():
  p = Program()
  p.TestPBKDF2()


if __name__ == "__main__":
  main()
