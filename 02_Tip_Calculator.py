
import math

bill = float(input('How much is the bill?: '))
tip = float(input('What percentage do you want to leave as a tip?: '))
people = float(input('How many people are you?: '))

tip = bill * tip / 100
tip_per_person = tip / people

print (f'The tip is {tip_per_person} per person')


