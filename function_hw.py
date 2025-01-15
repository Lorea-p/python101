'''
#exercise 1:
def birthday_message(name,age):
    message ="Happy birthday" + name + "i heard you are" + str(age) + "today!"
    return message
name= "Rebecca"
age=23
print(birthday_message(name,age))   


#exercise 2:
def drink_order(size, drink_type):
    message= "you ordered the" + size + drink_type
    return message
size="large"
drink_type="pepsi"

print(drink_order(size, drink_type))
'''
'''
#exercise 3:
def withdraw_cash(pin,balance, pin_attempt, amount):
    if pin_attempt ==pin:
        if amount<=balance:
            balance-=amount #balance= balance-amount we want to withdrawal
            #updates the balance by subtracting the amount to withdraw
            print("cash is being dispensed")
            print("new balace is", balance)
        else:
            print("insufficient funds. Unable to withdrawal")
    else:
             print("incorrect pin. transaction cancelled")   
def main():
     pin=1223   
     balance=50000
     pin_attempt=int(input("enter your pin:"))
     amount=float(input("enter the amount you want to withdrawal:"))    
     withdraw_cash(pin,balance, pin_attempt, amount)

if __name__=="__main__":  
         main()
'''
'''
#exercise 4:
favourite_sports=['netball','padel','badminton','basketball']
print(favourite_sports)
favourite_sports.append('dance')
print(favourite_sports)

first_four= favourite_sports[:4]
print(first_four)

only_one= favourite_sports[4]
print(only_one)

favourite_sports[favourite_sports.index('badminton')]='tennis'
print(favourite_sports)

favourite_sports.reverse()
print(favourite_sports)

favourite_sports.sort()
print(favourite_sports)

favourite_sports.remove('dance')
print(favourite_sports)

favourite_sports.clear()
print(favourite_sports)

'''

