
def descending_binary_search(data, left, right, value):
    if left==right:
        return None    
    middle = int((left+right)/2)
    if data[middle]==value:
        return middle    
    if (left+1 == right):
        return None
    if (value < data[middle]):
        return descending_binary_search(data, middle+1, right, value)
    else:
        return descending_binary_search(data, left, middle, value)
        
def ascending_binary_search(data, left, right, value):
    if left==right:
        return None    
    middle = int((left+right)/2)
    if data[middle]==value:
        return middle    
    if (left+1 == right):
        return None
    if (value > data[middle]):
        return ascending_binary_search(data, middle+1, right, value)
    else:
        return ascending_binary_search(data, left, middle, value)

def bitonic_search(data, left, right, value):
    if left==right:
        return None
    middle = int((left+right)/2)
    if data[middle]==value:
        return middle
    if (left+1 == right):
        return None    
    if (data[middle]>data[middle-1]):
        if (value > data[middle]):
            return bitonic_search(data, middle+1, right, value)
        else:
             result = ascending_binary_search(data, left, middle, value);
             if (result is not None):
                 return result
             result = descending_binary_search(data, middle+1, right, value);             
             if (result is not None):
                 return result
    else:
        if (value > data[middle]):
            return bitonic_search(data, left, middle, value)
        else:
             result = ascending_binary_search(data, left, middle, value);
             if (result is not None):
                 return result
             result = descending_binary_search(data, middle+1, right, value);        
             if (result is not None):
                 return result

input_data = [2, 3, 5, 7, 9, 11, 13, 15, 100, 8, 4, 1, 0]
print ('Input:', input_data)
search_value = 5
print ('Search value:', search_value)
N = len(input_data)
left = 0
right = N
index_result = bitonic_search(input_data, left, right, search_value)
print ('RESULT:')
print ('Index:', index_result)
if (index_result is not None):
    print ('Value:', input_data[index_result])