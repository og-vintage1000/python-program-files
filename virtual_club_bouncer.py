# Code for my virtual club bouncer - Practice

print("Welcome to Club Generic.")

age = int(input("Can I see your ID and confirm your age?"))

if age < 18:     
    # No entry for those under 18                                       # Must be done in order
    print("Access denied. Too young!")
elif age <=20:
    # If between the age of 18 and 20, can enter, but no drinking
    print("You can come in, but no drinking!")
else:
    # If 21+, can drink
    print("Welcome in! Enjoy your night.")
