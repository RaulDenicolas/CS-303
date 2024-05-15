#Raul Denicolas Completed 9/15

#1
fav_color = input('Favorite color?')
for i in fav_color:
    print(i)

#2
i=0
user_number = int(input('Pick a number:'))
while i <= user_number:
    print (i)
    i = i+1

#3
food = input('Pick an option of soup, salad, or sandwich:')
food = food.lower()
while food != 'soup' and food != 'salad' and food != 'sandwich':
    print('Sorry that\'s not an option!')
    food = input('Pick an option of soup, salad, or sandwich:')
print('Ok, you picked ' + food + '!')

#4 - Bonus
repeat_shape = int(input('How many times would you like to repeat the shape?'))
import turtle
t = turtle.Turtle()
i=0
while i < repeat_shape:
    t.circle(50)
    t.penup()
    t.forward(25)
    t.pendown()
    i = i+1
