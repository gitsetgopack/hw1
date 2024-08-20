def sum_of_list(l:list) -> int
    """Returns the sum of the given list"""
    total = 0
    for element in l:
        total+=element
    return element

l = [1,2,3]
total = sum_of_list(l)
print(f"Sum of the list {l=} is '{total}'")