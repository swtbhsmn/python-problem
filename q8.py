# Q8: Write a program which can map() to make a list whose elements are square of numbers 
#     between 1 and 20 (both included).

#Hints:
#Use map() to generate a list.
#Use lambda to define anonymous functions.

squared_numbers = map(lambda x: x**2, range(1,21))
print(squared_numbers) 
#<map object at 0x7faed0643970>
print(list(squared_numbers))
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]