
def leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
        print ('The year is leap')
    else:
        print('The year not is leap')

leap_year(2000)
leap_year(2001)
leap_year(2024)

