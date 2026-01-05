#exercise 10
def even_or_odd(num):
    if num % 2 == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd'
"""
this function checks whether the number is even or odd.
Using the modulo '%' operator to it determines if the 
number is divisible by 2. If there are no remainder, the 
number is even, if there is then it is odd. The return is used 
to sent the result back to the caller.
"""

def main():
    number = int(input('Please enter an integer: '))
    #gets input from user and converts it into a integer
    checker = even_or_odd(number)
    #calls the function above to check the inputted number
    print(checker)
    #displays the result

if __name__ == "__main__":
    main()
    #this executes the main function because the program run directly. 