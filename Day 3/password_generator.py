import random

print("Welcome to Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
symbols = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+']

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

password = ''
for char in range(1, nr_letters + 1):
  password +=  random.choice(letters)

for char in range(1, nr_symbols + 1):
  password +=  random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password +=  random.choice(numbers)

print(password)

password_list = list(password)

print(password_list)
password = ''

random.shuffle(password_list)
for char in range(0, len(password_list)):
  password += password_list[char]

print(f'Here is the shuffeled Password: {password}')
