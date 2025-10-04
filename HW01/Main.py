# get first number
while True:
  try:
    startNum = int(input("Enter first number: "))
    break
  except ValueError:
    print("You typed string, not a number. Try again.")

# get second number
while True:
  try:
    endNum = int(input("Enter second number: "))
    break
  except ValueError:
    print("You typed string, not a number. Try again.")

# check if numbers the same 
if startNum == endNum:
  print("First and second numbers must be different!")
  exit()

# get step number
while True:
  try:
    stepNum = int(input("Enter step number: "))
    if stepNum == 0:
      print("Step cannot be zero. Try again.")
    else: break
  except ValueError:
    print("You typed string, not a number. Try again.")

# check if step posible with numbers
if abs(endNum - startNum) % abs(stepNum) != 0:
  print("It's not possible to reach the second number with the given step")
  exit()

# print range
if startNum < endNum:
  for i in range(startNum, endNum + 1, stepNum):
    print(i, end=" ")
else:
  for i in range(startNum, endNum - 1, -stepNum):
    print(i, end=" ")
print()  
  