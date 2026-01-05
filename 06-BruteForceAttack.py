#exercise 6
print('Welcome Back, User1!')
#displays a welcome message 

password_correct = '12345'
attempt = 5
#the correct password and number of attempts allowed

while attempt > 0:
    password = input('Password: ')
    #the loops continues asking for password as long as the attempts doesn't reach zero.
    if password == password_correct:
        print('Access Granted!')
        break
        #once the password matches the correct one it will exit the loop and give access to the user.
    else:
        attempt -= 1
        #if the password didn't match this decrement the attempt counter
        if attempt > 0:
            print(f'Access Denied! You have {attempt} attempts remaining, please try again.')
            #informs the user how many attempts left.
        elif attempt == 0:
            print('The authorities have been alerted due to multiple failed log in attempts')
            #if it reaches zero or max attempt it displays a alert message. 
