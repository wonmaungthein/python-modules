# 1. Store a message in a variable, then print that message. 
message= "How are you?"
print(message)

# 2. Store a message in a variable, and print that message. Then change the value of your variable to a new message, and print the new message.
message1= "Message 1"
print(message1)

newMessage= f"This is new message {message1}"
print(newMessage)

# 3. Store a person’s name in a variable, and print a message to that person. 
name= "Won Thein"
print(f"Hello {name}, a message for you. {message}")

# 4. Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
nameInLowerCase= name.lower()
nameInUpperCase= name.upper()
nameInTitle= name.title()
print(f"Here is the name in lower case: {nameInLowerCase}")
print(f"Here is the name in uper case: {nameInUpperCase}")
print(f"Here is the name in Title case: {nameInTitle}")

# 5. Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results.
addNums= 2+2
subtractNums= 3-1
multipleNums = 2*2
divideNums= 4/2

print(addNums)
print(subtractNums)
print(multipleNums)
print(divideNums)

# 6. Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
favouriteNum = 7
myMessage = f"My favourite number is => {favouriteNum}"
print(myMessage)

# ---

# ## Stretch and Challenge 


# 1. Use an f-string to print out a message with a variable. 
print(myMessage)

# 2. Use multiple variables in one string to print a message.
print(f"Hello {name}, a message for you. {message} {myMessage}")

# 3. Set three variables, one that says, “Good”, another that says, “Day”, and another that says your name. “Add” them together, with a space between each word, and store it into another variable. Then, print out that variable. 
condition="Good"
day="Day"
myName="Won Maung Thein"
greeting=f"{condition} {day}, {myName}!"
print(greeting)