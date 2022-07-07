# 1 Apple  = 3 liras
# 1 kg apple has 5 apples

apple_price = 3
count = input("How many apples do you want?")
count = int(count)
total_price = apple_price * count
print("You are going to buy " + str(count) + " apples.")
print("You have to pay " + str(total_price) + " liras.")

