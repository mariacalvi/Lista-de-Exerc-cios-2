def filter_list(lst, func):
    return [elem for elem in lst if func(elem)]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


is_even = lambda x: x % 2 == 0

filtered_list = filter_list(my_list, is_even)
print("Filtered list (only even numbers):", filtered_list)
