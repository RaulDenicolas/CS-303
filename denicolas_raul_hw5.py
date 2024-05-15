#Created By:Raul Denicolas on October 10, 2022

#Create lists
chicken_soup = ['chicken', 'chicken broth', 'carrots', 'celery', 'noodles']
spaghetti = ['spaghetti noodles', 'pasta sauce', 'meatballs']
grilled_cheese = ['bread', 'butter', 'cheese']
garden_salad = ['lettuce', 'cucumber', 'carrots', 'olives']
rauls_special = ['greek yogurt', 'strawberries', 'blueberries', 'maple syrup', 'chia seeds']
#Ask for user input
ask_want_to_make = input('What would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
grocery_list = []
#if-statement to print lists
if ask_want_to_make.lower() == 'chicken soup':
    i = 0
    print('Chicken Soup:', end = ' ')
    while i < len(chicken_soup)-1:
      print(chicken_soup[i], end=', ')
      i+=1
    print(chicken_soup[len(chicken_soup)-1])
    ask_want_to_make_2 = input('What else would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
    grocery_list += chicken_soup
elif ask_want_to_make.lower() == 'spaghetti':
    i = 0
    print('Spaghetti:', end = ' ')
    while i < len(spaghetti)-1:
      print(spaghetti[i], end=', ')
      i+=1
    print(spaghetti[len(spaghetti)-1])
    ask_want_to_make_2 = input('What else would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
    grocery_list += spaghetti
elif ask_want_to_make.lower() == 'grilled cheese':
    i = 0
    print('Grilled Cheese:', end = ' ')
    while i < len(grilled_cheese)-1:
      print(grilled_cheese[i], end=', ')
      i+=1
    print(grilled_cheese[len(grilled_cheese)-1])
    ask_want_to_make_2 = input('What else would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
    grocery_list += grilled_cheese
elif ask_want_to_make.lower() == 'garden salad':
    i = 0
    print('Garden Salad:', end = ' ')
    while i < len(garden_salad)-1:
      print(garden_salad[i], end=', ')
      i+=1
    print(garden_salad[len(garden_salad)-1])
    grocery_list += garden_salad
    ask_want_to_make_2 = input('What else would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
    grocery_list += garden_salad
elif ask_want_to_make.lower() == 'rauls special':
    i = 0
    print('Raul\'s Special:', end = ' ')
    while i < len(rauls_special)-1:
      print(rauls_special[i], end=', ')
      i+=1
    print(rauls_special[len(rauls_special)-1])
    ask_want_to_make_2 = input('What else would you like to make? (Choose: Chicken Soup, Spaghetti, Grilled Cheese, Raul\'s Special) ')
    grocery_list += rauls_special

#Second if-statement
if ask_want_to_make_2.lower() == 'chicken soup':
    i = 0
    print('Chicken Soup:', end = ' ')
    while i < len(chicken_soup)-1:
      print(chicken_soup[i], end=', ')
      i+=1
    print(chicken_soup[len(chicken_soup)-1])
    grocery_list += chicken_soup
elif ask_want_to_make_2.lower() == 'spaghetti':
    i = 0
    print('Spaghetti:', end = ' ')
    while i < len(spaghetti)-1:
      print(spaghetti[i], end=', ')
      i+=1
    print(spaghetti[len(spaghetti)-1])
    grocery_list += spaghetti
elif ask_want_to_make_2.lower() == 'grilled cheese':
    i = 0
    print('Grilled Cheese:', end = ' ')
    while i < len(grilled_cheese)-1:
      print(grilled_cheese[i], end=', ')
      i+=1
    print(grilled_cheese[len(grilled_cheese)-1])
    grocery_list += grilled_cheese
elif ask_want_to_make_2.lower() == 'garden salad':
    i = 0
    print('Garden Salad:', end = ' ')
    while i < len(garden_salad)-1:
      print(garden_salad[i], end=', ')
      i+=1
    print(garden_salad[len(garden_salad)-1])
    grocery_list += garden_salad
elif ask_want_to_make_2.lower() == 'rauls special':
    i = 0
    print('Raul\'s Special:', end = ' ')
    while i < len(rauls_special)-1:
      print(rauls_special[i], end=', ')
      i+=1
    print(rauls_special[len(rauls_special)-1])
    grocery_list += rauls_special

#Print grocery list
i = 0
print('Grocery List:', end = ' ')
while i < len(grocery_list)-1:
    print(grocery_list[i], end=', ')
    i+=1
print(grocery_list[len(grocery_list)-1])

#Ask user for any additional inputs
additions_to_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished) ')
while (additions_to_list != 'Done'):
  grocery_list.append(additions_to_list)
  additions_to_list = input('Would you like to add any other items to your grocery list? (enter \'Done\' when finished) ')

#Print final grocery list
i = 0
print('Grocery List:', end = ' ')
while i < len(grocery_list)-1:
    print(grocery_list[i], end=', ')
    i+=1
print(grocery_list[len(grocery_list)-1])
