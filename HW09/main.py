from DataAccessor import DataAccessor

class Program:
  def __init__(self):
    try:
      self.data_accessor = DataAccessor()
    except RuntimeError as err:
      print(err)
      return
    
  def registration_user(self):
    print("--- Register new user ---")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    login = input("Login: ").strip()
    password = input("Password: ").strip()
    birthdate = input("Date birthday (yyyy-mm-dd, or skip): ").strip()

    if len(birthdate) != 10 or not birthdate.isdigit() and birthdate[4] != "-" and birthdate[7] != "-":
      birthdate = None

    try:
      user_id = self.data_accessor.register_user(name, email, login, password, birthdate)
      print(f"User registered successfully. ID = {user_id}")
    except ValueError as ve:
      print("Error during registration:", ve)
    except RuntimeError as re:
      print("Error during work with DB:", re)


  def authentication_user(self):
    print("--- User authorization ---")
    login_check = input("Login: ").strip()
    password_check = input("Password: ").strip()
    auth_result = self.data_accessor.authenticate(login_check, password_check)
    if auth_result:
      print("Authorization successful! User information:")
      print(auth_result)
    else:
      print("Incorrect login or password")


def main():
  p = Program()
  p.registration_user()
  p.authentication_user()

if __name__ == "__main__":
  main()
