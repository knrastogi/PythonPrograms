"""
Write a function that determines how many days there are in a particular month. Yourfunction will take two parameters: The month as an integer between 1 and 12, andthe year as a fourdigit integer. Ensure that your function reports the correct numberof days in February for leap years. Include a main program that reads a month andyear from the user and displays the number of days in that month.
"""
d1 = {2: 29}
numDays = {1: 31, 2: 28, 3: 31, 4:30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10:31, 11: 30, 12:31}
def countDays(month,yr):
    '''
    Display the number of days in a particular month of a year
    '''
    if (yr%4 == 0 and yr%100!=0) or (yr%400==0):
        numDays.update(d1)

        
    if month == 1:
        print("Your month is Jan, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 2:
        print("Your month is Feb, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 3:
        print("Your month is March, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 4:
        print("Your month is April, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 5:
        print("Your month is May, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 6:
        print("Your month is June, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 7:
        print("Your month is July, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 8:
        print("Your month is Aug, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 9:
        print("Your month is Sept, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 10:
        print("Your month is Oct, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 11:
        print("Your month is Nov, {} n and no of days are {}".format(yr, numDays[month]))
    elif month == 12:
        print("Your month is Dec, {} n and no of days are {}".format(yr, numDays[month]))
    else:
        print("Wrong month")

