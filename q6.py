#   Q6. Write a program using generator to print the numbers which can be divisible by 5
#   and 7 between 0 and n in comma separated form while n is input by console.

def number_generator(n):
   
     # iterate from 0 to n
    for j in range(1, n+1):
 
        # Short-circuit operator is used
        if j % 5 == 0 or j % 7 == 0:
            yield j

n = int(input('Enter number:'))
values = []
for i in number_generator(n):
    values.append(str(i))
print(",".join(values))


