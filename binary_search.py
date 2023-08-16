L = [40, 2, 21, 13, 23, 17, 11, 324, 112, 43, 5, 22, 1]

def binary_search(list_to_be_used, searched_value, left=0, right=None):
    if right is None:
        right = len(list_to_be_used) - 1
    
    #base condition for recursion - the element is not in the list
    if left > right:
        print("Value not found!")
        return False

    middle_index = (left + right) // 2
    middle_point = list_to_be_used[middle_index]
    
    if searched_value == middle_point:
        print(searched_value)
        return True
    elif searched_value < middle_point:
        return binary_search(list_to_be_used, searched_value, left, middle_index-1)
    else:  #searched_value > middle_point
        return binary_search(list_to_be_used, searched_value, middle_index+1, right)

#sort the list once before starting the search
L.sort()
binary_search(L, 5)
