import random

print('Password Generator \n')

n_letters = int(input ('How many letters would you like? \n'))
n_symbols = int(input ('How many symbols would you like? \n'))
n_numbers = int(input ('How many numbers would you like? \n' ))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','%','&','/','?']
numbers = ('1','2','3','4','5','6','7','8','9')

password_L = []

for char in range(1,n_letters + 1):
  password_L.append(random.choice(letters))

for char in range(1, n_symbols + 1):
   password_L.append(random.choice(symbols))

for char in range(1, n_numbers + 1):
   password_L.append(random.choice(numbers)) 

random.shuffle(password_L)  #shufle the list

password = ""  #string converter
for char in password_L:
   password += char

print(f"\nHere is your passaword: {password}")


