# 1.	Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
# question = 'What kind of rental car do you like? '
# message = "Let me see if I can find you a "

# answer = input(f'{question} \n')
# print(f'{message}{answer}.')

# 2.	Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
# question = 'How many people are in their dinner group?'
# reply = 'Sorry, you will have to wait for a table.'
# ready = 'Your table is ready.'

# answer = input(f'{question} \n')
# if int(answer) > 8:
#     print(reply)
# else:
#     print(ready)

# 3.	Ask the user for a number, and then report whether the number is a multiple of 10 or not.
# question = 'Give me a number!'
# multiple_of_10 = 'The number is a multiple of 10'
# not_multiple_of_10 = 'The number is not a multiple of 10'

# answer = input(f'{question} \n')
# if int(answer) % 10 == 0:
#     print(multiple_of_10)
# else:
#     print(not_multiple_of_10)

# 4.	Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
# prompt = 'What toppings do you like?'

# while True:
#     answer = input(f'{prompt} \n').lower()
#     if answer != 'quit':
#       print(f'You will add {answer} topping for your pizza')
#     elif answer == 'quit':
#        break

# 5.	A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
# prompt = 'What is your age? '
# under_3 = 'The ticket is free'
# between_3_and_12 = 'The ticket is $10'
# over_12 = 'The ticket is $15'

# while True:
#    input_answer = input(f'{prompt} \n')
#    answer = int(input_answer)
#    if answer < 3:
#       print(under_3)
#       break
#    elif answer >= 3 and answer <= 12:
#       print(between_3_and_12)
#       break
#    else:
#       print(over_12)
#       break

# 6.	Write a loop that never ends, and run it (if you dare!). (To end the loop, press ctrl-C or close the window displaying the output.)
answer = input('What is your name? \n')

while True:
    print(f'Hello {answer}')

# Stretch and Challenge
# If you complete the previous steps within the allotted time please move on to the following.
# ________________________________________

# 7.	Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# -	Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
# 8.	Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

