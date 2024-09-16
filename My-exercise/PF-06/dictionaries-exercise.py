# # Exercise 6: Dictionaries
# Please work through as many of the following exercises as you’re able to in the allotted time and upload the results of the last task you were able to complete.

# ### 1.
# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
# friend = {
#     'first_name':'Lynn',
#     'last_name':'Kubath',
#     'city':'Glasgow',
#     'age':22
# }
# print(friend)

# ### 2.
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
# favourite_number = {
#     'Joe': 2,
#     'Kay': 4,
#     'David': 7,
#     'Mike': 8,
#     'Stacy': 10
# }
# print(favourite_number)

# ### 3.
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. 

river_in_country = {
    'Nile': 'Egypt',
    'Amazon river': 'South America',
    'Ganges':'India'
}

# - Use a loop to print a sentence about each river, such as The Nile runs through Egypt. 
# for key,value in river_in_country.items():
#     print(f'The {key} runs through {value}')

# - Use a loop to print the name of each river included in the dictionary. 
# for key, value in river_in_country.items():
#     print(f'The river name is : {key}')

# - Use a loop to print the name of each country included in the dictionary
# for key, value in river_in_country.items():
#     print(f'The country name is : {value}')

# ### 4.
# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.
doggy = {
    'kind': 'dog',
    'owner':'Michael'
}
milly = {
    'kind': 'cat',
    'owner':'John'
}
sweety = {
    'kind': 'bird',
    'owner':'Jack'
}

# pets = [doggy, milly, sweety]
# for pet in pets:
#     print(pet)


# ### 5.
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
# favorite_places = {
#     'John':['Garden','New York', 'Dubai'],
#     'Mike':['Glasgow', 'London', 'Spain'],
#     'Julia': ['Spain','Tokyo','Myanmar']
# }

# for key, value in favorite_places.items():
#     for place in value:
#         print(f'{key} loves {place}' )

# ### 6.
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
# cities = {
#     'London':{
#         'country':'UK', 
#         'population':'15 million',
#         'fact':'Very busy'
#     },
#     'Glasgow':{
#         'country':'UK', 
#         'population':'5 million',
#         'fact':'beautiful'
#     },
#     'Edinburgh':{
#         'country':'UK', 
#         'population':'7 million',
#         'fact':'Lively'
#     }
# }
# print(cities)
# ## Stretch and Challenge
# If you complete the previous steps within the allotted time please move on to the following.

# - A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary. 
# glossary = {
#     'Python':'Programming language', 
#     'forLoop':'Looping the list and dictionary', 
#     'Print':'To print the code', 
#     'Condition':'Condtion for the statement', 
#     'List':'with a variety of items in the bracket'
# }

# print(glossary)

# - Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values. 

# - Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# - We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.



current_number = 1

while current_number <= 5:
    print(f'current number is {current_number}')
    current_number += 1
    print(current_number)
    print(f'current number is less than 5')
print('Done!')