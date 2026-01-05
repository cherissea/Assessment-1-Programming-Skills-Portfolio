#exercise 5
days_in_month = {
                1:31, #january
                2:28, #febuary
                3:31, #march
                4:30, #april
                5:31, #may
                6:30, #june
                7:31, #july
                8:31, #august
                9:30, #september
                10:31, #october
                11:30, #november
                12:31 #december
}
#key(month):value(days)

month = int(input('Please enter the a month number(1-12): '))
#ask user to input a number then converts it to a integer

if month >= 1 and month <=12:
#this condition makes sure that the number entered is in the range of 1-12
    if month == 2:
        #if the month is 2 it asks the user whether its a leap year or no
        leap_year = input('Is it a leap year? (yes/no): ').lower()
        #.lower() is used to convert any answer into lowercase 
        #if it is a leap year, it displays that febuary has 29 days. 
        if leap_year == 'yes':
            print('Month', month, 'has 29 days.')
        else:
            print('Month', month,'has', days_in_month[month],'days')
    else: #for the other months its proceeds to display the days within the month.
         print('Month', month, 'has', days_in_month[month], 'days')
else:
    print('Inavalid month number! Please enter a number from 1 - 12')