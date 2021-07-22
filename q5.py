# Q5. Write a binary search function which searches an item in a sorted list. The function
#     should return the index of the element to be searched in the list.

sorted_list_value = [1,23,56,89,78,87]

def binary_Search(sorted_list,find_element):
    start =0
    end = len(sorted_list)-1
    while start<=end:
        middle = start+(end-start)//2
        if sorted_list[middle]==find_element:
            return middle
        elif sorted_list[middle]<find_element:
            start = middle +1
        else:
            end   = middle -1
    return "Not Found!"

find_number = int(input("Enter number for search it's index:"))
print(binary_Search(sorted_list_value,find_number))
