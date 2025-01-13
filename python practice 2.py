'''
print("hello there")
'''
'''
age = "20"
age1="23"

print("tom is " + age)
print ("lorae is "+ age1)


car1, car2, car3 = "ferrari", "BMW", "Aston_ Martin"
print(car3)
'''
'''
#the below will not work because there are both strings and integers. 
#you cant put an integer into a string. they have to be the same
integer_example=10
print ("Tom is "+ integer_example)

#youd have to convert it into a string by adding ""
integer_example="10"
print ("Tom is "+ integer_example)
#tom is 10
###
'''
'''
integer_example2 =10
float_example=10.5

print(integer_example2 + float_example)
# 20.5
'''
'''
integer_example= "2"
string_example ="hello python"
boolean_example= True
float_example=10.5

print(integer_example, float_example, string_example, boolean_example)
# to add a full stop at the end you put a comma instead of +
print("my name is"+ integer_example , ".")

#'type' shows you the data type of the variable
print(type(string_example))

print(range(6))

'''
'''
#To make a list you use []
my_fav_actor= ["johnny depp","selena gomez","emma stone"]

# f formats it the way you want it to be printed, instead of using a + which is longer to create a sentence. 
print(f"my favourite actors are {my_fav_actor}")
#my favourite actors are ['johnny depp', 'selena gomez', 'emma stone']

#if we just want the first name youd add [0]. In python, index starts from 0. its the first element.
print(f"my favourite actor is {my_fav_actor[0]}")
#my favourite actor is johnny depp    

#adds a full stop
print(f"my favourite actor is {my_fav_actor[0]}.")
#my favourite actor is johnny depp. 
'''

#"Write a Python function to calculate the factorial of a given number.
def factorial(n):
    """
    Return the factorial of n, an integer >= 0.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result






def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # prepend each character
    return reversed_str

# Example usage:
original = "Hello World"
reversed_s = reverse_string(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_s}")
