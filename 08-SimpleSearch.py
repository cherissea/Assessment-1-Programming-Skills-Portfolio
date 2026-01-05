#exercise 8
name = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']
#list of names

def find_name(search_name):
#loops through each name to check if there are matches.
    for n in name:
        if n == search_name :
            return n
    #checks whether the name matches the search term
    return print('not found')
    #it informs  that there no match after checking the list

look = input('Enter the name you want to find: ').capitalize()
"""
.capitalize()  is used to match the user input with the list format. 
It capitalizes the first letter of the entered name.

"""

find_name(look) 
#calls the function to search the entered name 