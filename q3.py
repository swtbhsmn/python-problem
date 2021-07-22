# Q3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
#     after removing all duplicate values with original order reserved.
#     Hint: Use set() to store a number of values without duplicates.

list_value = [12,24,35,24,88,120,155,88,120,155]

def remove_duplicate(lists):
    update_list=[]
    unique_numbers = set()
    for item in lists:
        if item not in unique_numbers:
            unique_numbers.add( item )
            update_list.append(item)

    #print(unique_numbers) # {35, 12, 155, 24, 88, 120}
    return update_list    # [12, 24, 35, 88, 120, 155]

print(remove_duplicate(list_value))
