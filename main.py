# warm up
# get users first and last name
# print the name reverse order 
  # name1 = input("What is your first name? ")
  # name2 = input("What is your last name? ")
  # print("Your name is: " + name2, name1)
#--------------------------------------------------------

# Loops
# while loops

# while loop takes in a boolean experetion (T/F)
# Boolean operaters:
# Comparison operaters 
# let 3 = x
# x < 5 (less than 5)
# x > 5 (greater than 5)
# let x = 5
# x <= 5 (less than or equall to 5)
# x >= 5 (greater than or equall to 5)
# x == 5 (equall to 5)
# x != 5 (not equall to 5)

# Logical operaters
#and 
#or
#not

# A while loop will only run if the boolean experetion is true
# counter = 0
# while(counter <= 5):
#   print(counter)
#   counter = counter + 1

# for loops
# counter = 1
# for counter in range(6):
#   print(counter)

# counter = 0
# for counter in range(0, 5):
#   print(counter + 1)

#list od numbers 
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# # get the sum of all numbers
# for numbers in range(1, 6):
#   sum = sum + numbers 
#   print(sum)

#conditionals 
#--------------------------------------------
#definition: if x then y 
# ex. if I go to school then I will learn
# ex. if I drink and drive i will get into an accident 

#if statements are used for desition making. If statements only run if the boolean experetion is true

#template if <boolean experetion> 
# money = 5
# if money == 5:
#   print("I have 5 dollars!")
#   money = 10
#   if money == 10:
#     print("I gained 5 more dollars!")
# elif money == 6:
#   print("I have 7 dollars!")
# elif money == 7:
#   print("I have 7 dollars!")
# else:
#   print("I have a different amount of money")


season = input("What season is it right now? ")
if season == "winter":
  print("Stay warm!")
elif season == "fall":
  print("look at the colorful leaves")
elif season == "spring":
  print("go on a walk")
else:
  print("go to the pool!")
