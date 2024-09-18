# Files and Exceptions - Tasks


# 1.Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. 
# Start each line with the phrase In Python you can.... Save the file as learning_python.txt in the same directory as your exercises from this chapter. 
# Write a program that reads the file and prints what you wrote three times. 
# Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

with open('learning_python.txt') as file_object:
    content = file_object.read()
    for file in range(3):
        print(f'<==={file}===> \n{content}')


# 2.Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt. 
answer = input('What is your name?\n')
with open('guest.txt','w') as file_object:
    file_object.write(answer)
    print(f'New text {answer} is added to the guest.txt file')

# 3.Write a while loop that asks people why they like programming. 
# Each time someone enters a reason, add their reason to a file that stores all the responses.
while True:
    answer = input('Why do you like programming? \n')
    with open('reasons_I_like_programming.txt','a') as file_object:
        file_object.write('\n')
        file_object.write(f' \n {answer} \n')
        file_object.write('\n')
        break

# 4.Write a program that prompts the user to enter the name of a file. 
# Try to open the file for reading. If the file does not exist, catch the FileNotFoundError exception and print a message indicating that the file could not be found. 
# If the file exists, read its contents and display them.
file_name = input('Name a file \n')
file_to_open = f'{file_name}.txt'

try:
    with open(file_to_open) as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError:
    print('file not found')

# 5.Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
# -	Stretch and Challenge:  Modify your except block to fail silently if either file is missing.

try:
    with open('cats.txt') as cat_file_object:
        content = cat_file_object.read()
        print(content)

    with open('dogs.txt') as dogs_file_object:
        content = dogs_file_object.read()
        print(content)
except:
    print('No file is found')

# 6.Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, 
# “I know your favorite number! It’s _____.”
import json

favourite_number = input('What is your favourite number? \n')
with open('favourite_number.json','w') as json_file:
    json.dump(favourite_number,json_file)
    print(f'Data added to the json file is {favourite_number}')

with open('favourite_number.json','r') as read_json_file:
    content = read_json_file.read()
    print(f'I know your favorite number! It’s {content}')
