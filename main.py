# Jacobus Rothmann

print("Please enter the sentence you want to reverse:")
# Gets input from the user
userInput = input()
# Splits the input into a list
wordList = userInput.split()
# reverses the position in of the list
wordList = list(reversed(wordList))
print("The reverse of your input is:")
# prints out the reversed of the users input
print(" ".join(wordList))