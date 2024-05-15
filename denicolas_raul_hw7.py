#Created by Raul Denicolas on October 21, 2022
def get_average(list_of_num):
#1 Error Message
  try:
    return round(sum(list_of_num)/len(list_of_num))
  except ZeroDivisionError as err:
    print(err)
  
def main():
  numbers = [2,3,4,5]
#2 Error Message
  try:
    print(get_average(number))
  except NameError as err:
    print(err)
  word = 'Hello'
  for i in range(len(word)+1):
#3 Error Message
    try:
      print(word[i])
    except IndexError as err:
      print(err)
  numbers = []
  print(get_average(numbers))
#4 Error Message
  try:
    print(numbers[10])
  except IndexError as err:
    print(err)
#5 Error Message
  try:
    num = int(input('Enter the letter A: '))
  except ValueError as err:
    print(err)
  
if __name__=="__main__":
  main()
