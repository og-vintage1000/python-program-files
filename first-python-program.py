print("Hello, world!")
print()
print('Hello, world!')
print('Hello, world!')      # Need to maintain consistency with quotes (all double or all single quotes)
print('Hello, world!')      # Need to make sure the parenthesis match up; ( )) is no good
# print("We're just ordinary people.\n We don't know which way to go, yeah, hey\n 'Cause were ordinary people\n Maybe we should take it slow, hey, hey\n We're just ordinary people\n We don't know which way to go\n 'Cause we're ordinary people\n Maybe we should take it slow")
print("""We're just ordinary people
We don't know which way to go, yeah, hey
'Cause we're ordinary people
Maybe we should take it slow, hey, hey
We're just ordinary people
We don't know which way to go
'Cause we're ordinary people
Maybe we should take it slow""")    # Printing multiple lines using """ """
print("My name is Bond. ", end="")  # Make sure you don't forget comma; prevent new lines
print("James Bond.")
print("My","name","is","James","Bond.", sep="-")     # Using comma separator
print("Marco! ", end="")
print("Polo!")
print("Marco!", "Polo!", sep=" ")
print(27)                   # Integers or whole numbers
print(27.4)                 # Float values, contain decimals or exponents
print(True > False)         # Boolean values: true or false
print(True < False)
print(2+2)
print(2-2)
print(44*23)                # Mulitply
print(22/11)                # Gives answer in float value
print(22//11)               # Gives quotient
print(10%3)                 # Modulus; gives remainder
print(2**3)                 # Exponential calculation

name = "James Bond"
age = 45
height = 67

print("My name is " + name + ".")
# print("I am " + age + "years old.")       # Wont' work, can't concatenate string w/ integer
# print("I am " + height + "inches.")       # Wont' work, can't concatenate string w/ integer
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " inches.")
print("My name is " + name + ", " + "I am " + str(age) + " years old, and I am " + str(height) + " inches." )
# I am adding 6 inches to the height
height = height + 6
print("My name is " + name + ", " + "I am " + str(age) + " years old, and I am " + str(height) + " inches." )

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please input your height: "))
print("My name is " + name + ", " + "I am " + str(age) + " years old, and I am " + str(height) + " inches." )
