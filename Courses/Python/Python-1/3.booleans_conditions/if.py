# Control Flow = control what code is run based on the conditions that are satisfied
# if statement = gets executed only under a satisfied condition

# Create If Statements
# Write if, followed by a conditional expression and a colon (:)
# Code on next line will only run when condition is true
score = 100
if score == 100:
  print("You did it boi!")

# Many operators to create conditional expressions
# use (==) to see if 2 values are equal
# use (!=) to see if 2 values are not equal
score = 80
if score != 100:
  print("You tried hard, but good luck next time")
if score == 100:
  print("You did it man!")  

# If you don't give another condition, it prints blank
score = 50
if score == 100:
  print("Good job!")

# If we don't indent our code, it will return an indentation error
score = 69
if score == 100:
print("Good Job")  