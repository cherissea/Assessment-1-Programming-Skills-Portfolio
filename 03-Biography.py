#exercise 3
username = input('Please type your full name?: ')
#gets the user's full name

while True:
    userage = input('Enter your age?: ')
    if userage.isdigit():
        print('valid age')
        break
    else:
        print('Invalid')

"""
It asks for the user's age. 
The While loop validates the age input and repeats until the condition is met.
The if conditions checks if the input contains only digits, while the else
informs that it is invalid and asks the age again.
"""
        
userhometown = input('Where is your hometown? (city, capital, country): ')
#gets user hometown

biography = {'name': username, 'age': userage, 'hometown': userhometown}
#the user inputs are stored in a dictionary as key-value pairs

print(biography['name'], biography['age'], biography['hometown'], sep='\n')
"""
the sep='\n' parameter displays each values on a seperate line using a one single print statement
"""
