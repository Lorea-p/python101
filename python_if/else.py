'''
age=10
if age==11:
    print("Age is 11")

#we can change or our condition to get an output as the 
#above gave us nothing

age =11 
if age ==11:
    print("Age is 11")
    #Age is 11

a =15
b=80
if b>a:
    print("b is greater than a")


#check if a number is even
number=8
if number %2==0: # % means if we divide the number by 2 and get NO REMAINDER,
# then that number is an even number 
    print("Number is an even number")
#Number is an even number
#condition is true, so gives an output

#i want to check if this list is empty or not
favourite_food=[1,3,5]
if favourite_food ==[]:
    print("List is empty")
#no output as list is no empty

#now putting IF/ELSE:
favourite_food2=[1,3,5]
if favourite_food2 ==[]:
    print("List is empty")
else:
    print("List is not empty")


#write a script to compare two numbers
n1= 2
n2=3
if n1>n2:
    print("n1 is greater than n2")
else:
    print("n2 is greater than n1")

number=13
if number %3==0:
    print("number is odd")
else:
    print("number is even")

#using ELIF for multiple conditions
grade=75
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
else:
    print("D or below")
 #when you have two conditions like true or false, use ELSE
 #when having multiple if/else categories like grades, use ELIF

'''

'''
# FOR loops
for item in [1,2,3,4,5,6,'hi']:
    print(item)



# WHILE loop
#keeps running until a condition is true

#count down from 10
i =100
while i >=0:
    print(i)
    i-=10  #taking away 10 from i or can be written as i=i-10
#100
#90
#80
#70
#60
#50
#40
#30
#20
#10
#0
#keeps printing it until it reaches 0

i =0 
while i<=100:
    print(i)
    i+=10  #its now adding 10.
#0
#10
#20
#30
#40
#50
#60
#70
#80
#90
#100


'''
'''
#infinite loop and break

while True:  #causes an infinite loop, which doesnt stop and keep running
    print('Infinite Loop')
    break # will only run once.it stops it

i=10
while i ==10: # it will keep running as its checking
    #if its true and it keeps going because 10 is always = to i
    print('infinite loop')
'''
'''
num=0
while True:
    print('Number:', num)
    if num ==10:
        break

'''

'''
import random
number = random. randint(1,10)## RANDINT generates a  random number between 1-10(inclusive)
#print(number)   # to see what number it has chosen, basically cheat
#allow the user three attempts to guess the number
for _ in range(3): #lets user have 3 attempts
    
    #get a guess from the user
    guess= int(input('Guess a number:')) # INT converts any string into an integer

    #check if guess is correct
    if guess == number:
        print('correct!')
        break #exit the loop if the guess is correct
    else:
        print('try again!') #prompt user to try again if the guess is incorrect
else:  # if the loop completes three iterations without a correct guess, print game over
    print ('game over!, the correct was', number)

'''
'''
#clues in the game
 #if you want it to print, ' number is lower than answer'
import random
number=random.randint(1,10)
for i in range (3):
    guess =int(input('guess the number:'))

    if guess == number:
        print('correct')
        break
    elif guess> number:
        print('the number is smaller')
    else:
        print('the number is bigger')
else:
    print('game over, the correct was', number)


#version control in visual studio code

'''
