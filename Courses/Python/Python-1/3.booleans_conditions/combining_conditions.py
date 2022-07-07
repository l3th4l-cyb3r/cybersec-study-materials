# We can use the and operator to combine coditions

# Here I am making a simple life schedule 
hour = 7
if hour>6 and hour<8:
  print("You woke up on the right time")
elif hour<6:
  print("You need to improve your sleeping schedule")
else:
  print("You need to be punctual so as to increase your productivity!")

hour=12
if hour == 12 or hour == 1:
  print("It's lunch time. Please go have lunch.")

hour=20
if not hour == 20 or hour == 21:
  print("It's not yet dinner time")
if hour == 20 or hour == 21:
  print("It's dinner time! Please go have dinner so that you can stay healthy")
