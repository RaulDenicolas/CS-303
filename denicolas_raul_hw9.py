#Initialize an intance of the get_average class, with list_to_average as a parameter from the main function
def get_average(list_to_average):
  #Use a variable to keep track of the total amount from the list that was given by the user
  total = 0
  #Initiate a for-loop that loops through each item in the list that was given
  for i in list_to_average:
    #Add to the amount total for each item in the list
    total = total + i
 #Return the rounded amount from the total amount divded by the number of items that were on the given list
  return round(total/len(list_to_average))
  
#Initialize an intance of the bubble_sort class, with sorting_list as a parameter from the main function
def bubble_sort(sorting_list):
 #Use a variable n, to keep track of the length of the list that was given
  n = len(sorting_list)
 #Initiate a for-loop that loops through a range of the number of items in the list that was given, goes thorugh all items
  for i in range(n-1):
    #Initiate a for-loop that skips the last item in the list, and goes through each item in the list from first to n-i-1
    for j in range(0, n-i-1):
        #Swithc an item if it is greater than the next element
      if sorting_list[j] > sorting_list[j + 1] :
        sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

#Initialize an intance of the is_prime class, with num as a parameter from the count_primes class
def is_prime(num):
    #Initiate an if-statement that compares the number that was given with the number two
    if num < 2:
    #If the numebr that was given is less than 2, then return False
        return False
    #Use a variable to keep track of a counter that stores the number you get from subtrating the number that was given with 1
    counter = num-1
    #Initiate a while loop that compares counter and the number 1
    while(counter > 1):
        #if the number that was given where to be divded by the counter variablem and has a remainder of zero...
        if num % counter == 0:
            #...then return Flase
            return False
        #Subtract counter by 1
        counter -= 1
    #If the counter passes the while-loop, then return True
    return True

#Initialize an intance of the count_prime class, with list_of_primes as a parameter from the main function
def count_primes(list_with_primes):
  #Use a variable to keep track of the total number of prime numbers found in a list
    primes = 0
    #Initiate a for-loop that for each item in the list that was given
    for x in list_with_primes:
        #Initiate an if-statement that calls on the is_prime class
        if(is_prime(x)):
            #if is_prime returns True, then add 1 to the primes varaible count
            primes += 1
    #Return the number of primes that were counted on the list that was given as a parameter
    return primes
  
#define the main function
def main():
  #create an empty list to populate with the user's input
  user_list = []
  #create variable x that asks the user to enter a number, whih then stores the users' input until they have entered the word 'Done'
  x = input('Enter a number (type "Done" when finsished): ')
  #Create a while loop that compares the input that the user put into the variable x, and then compares it to the sting 'done', and will continue until it equals that string
  while(x.lower() != 'done'):
  #Begin a try-execpt statement
    try:
    #The program will try to store an integer variable input x, and store it into a new variable x
      x = int(x)
      #The program will then add the new variable x into the user_list list
      user_list.append(x)
    #End the try-except statement, and if the program has a Value Error, store it as err
    except ValueError as err:
      #Display the Value Error, as well as a statement to the user that what they inputed was not a number
      print(err,'That was not a number!')
    #Once the user successfully goes through the try-except, they will be promted to enter a new interger, that will be stored in the x variable
    x = input('Enter another number (type "Done" when finsished): ')
    
  #Display the list that the user has inputed
  print('Your list:',user_list)
  #Display the number of prime numbers that the user inputed in thier list
  print('Your list has',count_primes(user_list),'primes')
  #Display the overall average of the list that the user inputed
  print('Average:',get_average(user_list))
  #Call the bubble_sort Class and pass the user's list as a parameter, in order to sort the list
  bubble_sort(user_list)
  #Display the now sorted list that the user has inputed
  print('Your list sorted:',user_list)

#check if this is the main module
if __name__=="__main__":
  #run the main function (which should always run first)
  main()
