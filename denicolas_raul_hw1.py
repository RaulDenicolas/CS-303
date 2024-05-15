#Raul Denicolas Completed: Sep 6, 2022
#Start off with an introduction
print("Hello! This story will involve you making decision on how your morning will unfold.")

#Begin with first decision
breakfast_choice = input("Will you have breakfast? (yes or no)")

if breakfast_choice.lower() == ("yes"):
  print("Great choice! Breakfast if the most important meal of the day.")
  breakfast_food = input("Since you said yes to having breakfast, what will you be having this morning?")
  if breakfast_choice.lower() == ("yes") and breakfast_food.lower() == ("oatmeal"):
    print(breakfast_food, "has many health benefits and keeps you full.")
  elif breakfast_choice.lower() == ("yes") and breakfast_food.lower() == ("eggs"):
    print(breakfast_food,"have alot of protein. Great choice for strong muscles!")
  elif breakfast_choice.lower() == ("yes") and breakfast_food.lower() == ("cereal"):
    print(breakfast_food,"can have alot of sugar, but who cares! Treat yourself today!")
  elif breakfast_choice.lower() == ("yes") and breakfast_food.lower() == ("avacodo toast"):
    print(breakfast_food,"is very trendy and healthy!")
  else:
    print("You choose and unconventional breakfast food. That makes you unique!")
else:
  print("You choose to skip breakfast. That's okay, maybe you aren't that hungry.")

#Next, lets see what you want to wear today
print("Now that the breakfast situation is cleared up lets see what you want to wear today.")

clothes_choice = input("Do you want to be comfortable or stylish today?")

if clothes_choice.lower() == "stylish":
  print(clothes_choice,"is great! Let's see what you got in your closet.")
  favorite_color = input("Now that you opened your closet, what color are you feeling ike today?")
  if clothes_choice.lower() == "stylish" and favorite_color.lower() == "red":
    print("Red is SO powerful! You are going to have a productive day.")
  elif clothes_choice.lower() == "stylish" and favorite_color.lower() == "blue":
    print("Blue is so claming! You are going to have a peaceful day.")
  elif clothes_choice.lower() == "stylish" and favorite_color.lower() == "yellow":
    print("Yellow is happy! You are going to make so many freinds today.")
  else:
    print("You choose a non-primary color. You will stand out today!")
elif clothes_choice.lower() == "comfortable":
  print(clothes_choice,"makes you happy. Put on an oversized sweather to stay warm.")
else:
  print("You didn't pick a choice. That's okay, stay in your PJ's!")
  
#Lastly, let's see if you want to stay at home, or go out
home_outside = input("Okay, now for the final choice. Will you be staying home or going outside today?")

if (home_outside.lower() == "staying home"):
  print(home_outside, "is the best. Have a self-care day!")
elif (home_outside.lower() == "going outside"):
  print(home_outside, "is awesome. Go get some of that sun!")
else:
  print("You didn't pick a choice. That's okay, maybe we can decide later!")
