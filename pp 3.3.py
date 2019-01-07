print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("PRACTICE PROBLEM 3.3")
##Translate these into Python if/else statements:

###(a) If year is divisible by 4, print 'Could be a leap year.'; otherwise print 'Definitely nota leap year.'
leap_year = int(input("Please enter the year:"))

if leap_year % 4 == 0:
    print('It is a leap year.')
else:
    print('It is not a leap year. ')


###(b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck nexttime...'
ticket = input('Enter code: ')
lottery = ['10', '30', '50']

if ticket in lottery:
    print('You won.')
else:
    print('Better luck next time.')
