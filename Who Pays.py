import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#x=len(names)

#person = random.randint(0,x-1)

#who_pays=names[person]

#print(who_pays + " is going to buy the meal today!")

#or
person = random.choice(names)
print(person + " is going to buy the meal today!")