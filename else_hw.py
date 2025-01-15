#exercise 1:
number=6
if number %2==0:
    print("The number is even")

number=3
if number%2==0:
    print("The number is even")


#exercise 2:
my_list=[1,2,3,4,5,6,7,8,9]
if len(my_list)==0:
    print("list is empty")


#exercise 1: ELSE statement
number=7
if number %2==0:
    print("the number is even")
else:
    print("the number is odd")

#ELIF statement
#exercise 1
temperature=15.07
if temperature<=0:
    print("its freezing colddd!")
elif temperature<=10:
    print("its cold")
elif temperature<=20:
    print("its moderate")
elif temperature<=25:
    print("its warm")
else: print("its hotttt!")


#FOR loop
#exercise 1
string='hello world'
for char in string:
    print(char)

#exercise 2:
squares=[i**2 for i in range(1,11)]
print(squares)

#WHILE loop
#exercise 1
total_sum=0
current_number=1
while total_sum<100:
    total_sum+=current_number
    current_number+=1   #adds 1 to the current number
    print('the sum of numbers until reaching 100 is:', total_sum)

#exercise
import random
number=random.randint(1,10)
for _ in range(4):
    guess=int(input('guess the number:'))
    if guess==number:
        print('you guessed the number!')
        break
    else:
        print('try again')
else:
    print('you ran out of guesses, the number was:', number)

