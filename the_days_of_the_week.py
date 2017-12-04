# Created by: Kay Lin 
# Created on: 28th-Nov-2017
# Created for: ICS3U
# This program displays entering favourite number then showing the day

from enum import Enum

# an enumerated type of the days of the week
def the_days_of_the_week(favourite_number):
    # input your favourite day
    
    week = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    
    #input_day = input_day.upper()
    
    return week[favourite_number]
    
# input
print('Sunday(1), Monday(2), Tuesday(3), Wednesday(4), Thursday(5), Friday(6), Saturday(7)')
day_selected = int(input('Enter your favorite day of the week #: '))

# output
if day_selected >= 0 and day_selected <= 6:
    favourite_day = the_days_of_the_week(day_selected-1)
    print('Your favourite day of the week is: ' + str(favourite_day))
else:
    print('Please input valid number between 0 and 6.')

print('\n')




