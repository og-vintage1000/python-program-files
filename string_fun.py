word1 = input("Type down any word: ")                           # Input any word
print("This word has " + str(len(word1)) + " characters.")
print()
print("Let's make the word all uppercase.")         
print(word1.upper())                                            # Make given word all uppercasae
print()
print("Let's repeat the word multiple times.")
count = int(input("How many times do you want to repeat your given word: "))    # Input the number of times you want to repeat this word
repeat = word1 * count                                                          # Tells us how many times word will be repeated based on input
print(repeat)                                                                   # Repeats the word with no spacing
repeat1 = " ".join([word1] * count)
print(repeat1)                                                                  # Repeats the word with spacing
print()
for _ in range(count):
    print(word1)                                                                # Repeats the word in next line

