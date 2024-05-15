def add_space_and_capitalize(word):
    new_word = ''
    for i in word:
        new_word = new_word + i.upper() + ' '
    return (new_word)
  
def accrue_interest(loan_ammount):
    loan_balance = loan_ammount
    loan_intrest = loan_ammount * .06
    loan_balance = loan_balance + loan_intrest
    return (loan_balance)
  
def make_payment(loan_balance,payment_ammount):
    remaining_balance = 0
    if loan_balance <= payment_ammount:
        print('Paid Off!')
    else:
        remaining_balance = loan_balance - payment_ammount
        print('Paid ${0:.2f}'.format(payment_ammount))
    return (remaining_balance)
  
def display_balance(loan_balance):
  print('Current Balance ${0:.2f}'.format(loan_balance))
  
#### DO NOT CHANGE ANYTHING BELOW THIS LINE###
def main():
  big_text = 'finance'
  print(add_space_and_capitalize(big_text))
  loan = 12000
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,2000)
  display_balance(loan)
  loan = accrue_interest(loan)
  display_balance(loan)
  loan = make_payment(loan,12000)
  display_balance(loan)
  
if(__name__=="__main__"):
  main()
