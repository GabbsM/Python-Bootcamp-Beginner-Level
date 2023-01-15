import random
import numpy as np
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#letter:
letters_password =[]

for i in range(0,nr_letters):
  letter= random.choice(letters)
  letters_password.append(letter)

#numbers:
number_password = []
for number in range(0,nr_numbers):
  numb = random.choice(numbers)
  number_password.append(numb)

#symbols:
symbol_password = []
for symbol in range(0,nr_symbols):
  symb = random.choice(symbols)
  symbol_password.append(symb)

#password
password = letters_password + number_password + symbol_password
password_random = [password[np.random.randint(low=0,high=len(password))] for i in range(len(password))]
real_password = ''.join(password_random)
print(f'Password generated: {real_password}')