# We're trying to generate a list containing multiples of 3

# Initialize an empty list
list = []

# The range of values is from 1 to 20
for i in range(1, 20):
    # Use modulus to obtain a remainder of 0
    if i % 3 == 0:   
    # Extra message here showing which numbers are multiples of 3                       
        print(i, " is a multiple of 3.")
        # Each value of i that holds true for the condition is place into the list
        list.append(i)
    else:
        continue

# Placed print command outside of loop for final list result; made the list a readable string
print("The values between 1 and 20 that are multiples of 3 are " + str(list) + ".")

