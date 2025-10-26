def parse_ini(filename:str) -> dict | None:
  try:
    with open(filename, encoding="utf-8") as file:
      return { k:v for k, v in (
        map(
          str.strip,
          line.split(':', 1)
        )
        for line in (
          ln.split('#', 1)[0].split(';', 1)[0].strip() # clear spaces and comments
          for ln in file
        )
          if ':' in line
      )}
  except OSError as err:
    print("Error read file:", err)
    return None


def main() -> None:
  text = parse_ini("db.ini")
  print(text)


if __name__ == '__main__':
  main()

