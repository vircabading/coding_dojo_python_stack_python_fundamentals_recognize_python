"""//////////////////////////////////////////////////////       # Multi line comment
Subj:   Coding Dojo > Python Stack > Python > Fundamentals > Recognize Python
By:     Virgilio D> Cabading Jr.    Created: October 24, 2021
/////////////////////////////////////////////////////////"""

num1 = 42                                       # Variable declaration, number primitive data type, initialize           
num2 = 2.3                                      # Variable declaration, number primitive data type, initialize
boolean = True                                  # variable declaration, boolean primitivedata type, initialize
string = 'Hello World'                          # variable declaration, string primitive data type, initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
                                                # variable declaration, list composite data type, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
                                                # variable declaration, dictionary composite data type, initialize
fruit = ('blueberry', 'strawberry', 'banana')   # variable declaration, tuple composite data type, initialize
print(type(fruit))                              # type method returns class type of argument, prints class tuple
print(pizza_toppings[1])                        # access value of list composite data type
pizza_toppings.append('Mushrooms')              # append method adds an item at the end of a list
print(person['name'])                           # access value of dictionary composite date type using a key
person['name'] = 'George'                       # change value of dictionary composite data type using a key
person['eye_color'] = 'blue'                    # initialize value of dictionary composite data type using a key
print(fruit[2])                                 # access value of tuple composite data type using an index

if num1 > 45:                                   # if conditional, access value of number primitive data type
    print("It's greater")                       # function that prints a string
else:                                           # else conditional
    print("It's lower")                         # function that prints a string

if len(string) < 5:                             # if conditional, len funtion, returns the number of characters in a string
                                                # access value of a string primitive data type
    print("It's a short word!")                 # function that prints a string
elif len(string) > 15:                          # else if contditional (note elif is short hand for else if)
                                                # len function, retrurns the number of characters if a string is passed as a parameter
    print("It's a long word!")
else:                                           # else conditional
    print("Just right!")

for x in range(5):                              # for loop, start at 0, stop at 6, increment by 1
                                                # range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    print(x)                                    # prints a number
for x in range(2,5):                            # for loop, start at 2, stop at 5, increment by 1
    print(x)                                    # prints a number
for x in range(2,10,3):                         # for loop, start at 2, stop at 10, increment by 3
    print(x)                                    # prints a number

x = 0                                           # number primitive date type initialize 
while(x < 5):                                   # while loop, start at 0, end at 5
    print(x)
    x += 1                                      # while loop increment by 1

pizza_toppings.pop()                            # pop() removes and returns the last value from the list
pizza_toppings.pop(1)                           # pop(index) removes and returns the value from the list at the given index

print(person)                                   # prints a dictionary
person.pop('eye_color')                         # pop('key') removes and returns the value of the element in the dictionary with the given key
print(person)                                   # prints dictionary which no longer includes 'eye_color'

for topping in pizza_toppings:                  # for loop, start at 'Pepperoni", ends at cheese
    if topping == 'Pepperoni':                  # if conditional
        continue                                # continue skips the next three lines to the next incrementation of for loop
    print('After 1st if statement')
    if topping == 'Olives':
        break                                   # break stops the for loop

def print_hello_ten_times():                    # function declaration
    for num in range(10):                       # for loop, start at 0, end at 10, increment by 1
        print('Hello')

print_hello_ten_times()                         # execute function

def print_hello_x_times(x):                     # function declaration with x as a parameter
    for num in range(x):                        # for loop, start at 0. end at x value, increment by 1
        print('Hello')

print_hello_x_times(4)                          # execute function that prints hello four times

def print_hello_x_or_ten_times(x = 10):         # function declaration with x as a parameter with a default value of 10 if no parameter is passed
    for num in range(x):                        # for loop, start at 0, end at x value, increment by 1
        print('Hello')

print_hello_x_or_ten_times()                    # calls function with x defaulting to 10 since no parameter is passed
print_hello_x_or_ten_times(4)                   # calls funtion with 4 as the value of parameter x


"""
Bonus section
"""

# print(num3)                                   # name error, num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry'                        # error, tuple value cannot be changed
# print(person['favorite_team'])                # error, key does not exist in dictionary
# print(pizza_toppings[7])                      # index error, list index out of range
#   print(boolean)                              # indentation error, unexpected indent
# fruit.append('raspberry')                     # error cannot add value to tuple
# fruit.pop(1)                                  # error cannot delete value from tuple