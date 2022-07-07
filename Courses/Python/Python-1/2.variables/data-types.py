# There are different data types
print(69+420)
# calculates the sum
print("69"+"420")
# concatenates strings

# We can't concatenate strings and integers
# price = 120
# print("One kilo of apple costs " + price + "rupees")
# error comes like this: can only concatenate str (not "int") to str

# therefore, we have to perform type conversion
# convert integer to a string - str()
price = 120
print("One kilo of apple costs " + str(price) + " rupees")

## convert string to integer - int()
count = 69
price = 100
total_price = price*int(count)
print("Your total price will be " + str(total_price) + " rupees")