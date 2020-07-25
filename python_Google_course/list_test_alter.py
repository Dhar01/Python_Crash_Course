def skip_elements(elements):
    # code goes here
    new_list=[]  #initialize destination list
    # enumerate over list. i is the index and e is the actual element
    for i, e in enumerate(elements): 
        if i % 2 != 1: #Check if index position is odd or even
            # this will select only elements at positions 0, 2, 4...
            new_list.append(e)  #if so append the element to end
    return new_list
    
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
