L = [40, 2, 21, 13, 23, 17, 11, 324, 112, 43, 5, 22, 1]

def binary_search(list_to_be_used, searched_value):
    list_to_be_used.sort()
    middle_point = list_to_be_used[len(list_to_be_used)//2]
    
    if searched_value == middle_point:
        print(searched_value)
    
    if searched_value != middle_point:
        
       if searched_value < middle_point:
           
           list_to_be_used = list_to_be_used[:list_to_be_used.index(middle_point)]
           print(list_to_be_used)
           binary_search(list_to_be_used, searched_value)
           
       elif searched_value > middle_point:
           list_to_be_used = list_to_be_used[list_to_be_used.index(middle_point):]
           print(list_to_be_used)
           binary_search(list_to_be_used, searched_value)
           
       else:
            return False
           

binary_search(L, 5)

