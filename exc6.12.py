intersection = lambda list1, list2: list(set(list1) & set(list2))

list_a = [5, 4, 3, 2, 1]
list_b = [3, 4, 5, 6, 7]
result = intersection(list_a, list_b)
print("Common elements between list_a and list_b:", result)
