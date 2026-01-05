#exercise 4
"""
a question is asked and the answer is taken by user input
 The answer is validated using if and else conditions to c
check if it is correct or not. Using .lower() allows 
the user to type the answer in any case and converts it 
to lower case. Once the answer is correct, a point is added 
to the score, which at the end gives the toteal score. 
"""
score = 0

Q1 = input('What is the Capital of Italy?: ')
if Q1.lower() == 'rome':
    print('Correct!')
    score += 1
else: 
    print('Incorrect! The capital of Italy is Rome')
    
Q2 = input('What is the Capital of Belgium?: ') 
if Q2.lower() == 'brussels':
    print('Correct!')
    score += 1
else: 
    print('Incorrect! The capital of Belgium is Brussels')

Q3 = input('What is the Capital of Switzerland?: ')
if Q3.lower() == 'bern':
    print('Correct!')
    score += 1
else: 
    print('Incorrect! The capital of Switzerland is Bern')


Q4 = input('What is the Capital of Denmark?: ') 
if Q4.lower() == 'copenhagen':
    print('Correct!')
    score += 1
else: 
    print('Incorrect! The capital of Denmark is Copenhagen')

Q5 = input('What is the Capital of Norway?: ')
if Q5.lower() == 'oslo':
    print('Correct!')
    score += 1
else: 
    print('Incorrect! The capital of Norway is Oslo')

Q6 = input('What is the Capital of Greece?: ')
if Q6.lower() == 'athens':
    print('Correct')
    score += 1
else: 
   print('Incorrect! The capital of Greece is Athens')
    
Q7 = input('What is the Capital of United Kingdom?: ')
if Q7.lower() == 'london':
    print('Correct')
    score += 1
else: 
   print('Incorrect! The capital of United Kingdom is London')
    
Q8 = input('What is the Capital of Hungary?: ')
if Q8.lower() == 'budapest':
    print('Correct')
    score += 1
else: 
   print('Incorrect! The capital of Hungary is Budapest')
    
Q9 = input('What is the Capital of Ireland?: ')
if Q9.lower() == 'dublin':
    print('Correct')
    score += 1
else: 
   print('Incorrect! The capital of Ireland is Dublin')
                                   
Q10 = input('What is the Capital of Portugal?: ')
if Q10.lower() == 'lisbon':
    print('Correct!')
    score += 1
else: 
   print('Incorrect! The capital of Portugal is Lisbon')

print(f'Congratulations! You got {score} questions correct')