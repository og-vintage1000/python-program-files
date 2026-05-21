name = "Brian"          # Declaring a variable for name, with my name as a string
age = 45                # Declaring a variable for age, with the age as an integer
height = 1.70           # Declaring a variable for height, with my height in meters as a float value

print("Hello, my name is " + name + ". I am " + str(age) + " years old and " + str(height) + " meters tall.")   # Concatenation to display sentence

greeting = f"Hello, my name is {name}. I am {age} years old and {height} meters tall."      # Using f-string instead of concatenation
print(greeting)                                                                             # Using print to display f-string

print()

age = age + 5               # Adding 5 years to my current age
future = f"In 5 years, I will be {age} years old."
print(future)

print()

width = 5.5                 # Assigning values for the width and height of a rectangle
height1 = 2
area = width * height1      # Multiplying to acquire the area of a rectangle

multiply = f"The area of a {width} x {height1} rectangle is {area}."
print(multiply)

print()

num1 = 25                       # Assigning values for num1 and num2                             
num2 = 11
add = num1 + num2               # Applying operations for the following variables
subtract = num1 - num2
multiply1 = num1 * num2
divide = num1 / num2
quotient = num1 // num2
remainder = num1 % num2
numbers = f"The first number is {num1} and the second number is {num2}."
print(numbers)
print("Addition gives us " + str(add) + " and subtraction gives us " + str(subtract) + ".")
print("Muliplication gives us " + str(multiply1) + ".")
print("Division gives us " + str(divide) + " in decimal form, where our quotient is " + str(quotient) + " and our remainder is " + str(remainder) + ".")
# Displaying the result of each mathematical operation
