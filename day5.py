#PYPASSWORD GENERATOR

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

#EASY LEVEL ORDER WISE
#nr_symbols=int(input("How many symbols would you like?\n"))
#nr_numbers=int(input("How many numbers would you like?\n"))
#s=''
#for i in range(0,nr_letters):
#    r=random.randint(0,len(letters)-1)
#    s+=letters[r]
#for i in range(0,nr_symbols):
#    r=random.randint(0,len(symbols)-1)
#    s+=symbols[r]
#for i in range(0,nr_numbers):
#   r=random.randint(0,len(numbers)-1)
#    s+=numbers[r]
#print(s)

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))
password=[]
for i in range(0,nr_letters):
    password.append(random.choice(letters))
for i in range(0,nr_symbols):
    password.append(random.choice(symbols))
for i in range(0,nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
for char in password:
    print(char,end='')