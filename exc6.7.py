def find_largest_value(lst):
    if len(lst) == 0:
        return None  
    
    largest = lst[0] 
    
    for item in lst:
        if item > largest:
            largest = item
    
    return largest

my_list = [10, 5, 7, 20, 3]
largest_value = find_largest_value(my_list)

print("Largest value in the list:", largest_value)
