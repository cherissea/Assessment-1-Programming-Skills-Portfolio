#exercise 7
"""
for loop is a loop used when you know how many iterations is needed.
(n,n,n) the first n the parenthesis tells where to start, 2nd n is for where to end, 
and the 3rd is the step (increment/decrement value between each iteration). 

"""
#exercise 7.0 counts from 0-50, incrementing by 1 each time.
for count in range(0,51,1):
    print(count)

#exercise 7.1 counts backwards decrementing by 1.
for count in range(50,-1,-1):
    print(count)

#exercise 7.2 starts from 30 ends in 50, incrementing by 1. 
for count in range(30,51,1):
    print(count)

#exercise 7.3 counts backward but prints even number because its is decrementing by 2 
for count in range(50,9,-2):
    print(count)

#exercise 7.4 prints multiples of 5 from 100 to 200
for count in range(100,201,5):
    print(count)
    