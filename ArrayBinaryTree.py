binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_index(index):
    return 2 * index +1

def right_index(index):
    return 2 * index + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None
    
    

right = right_index(0)
left_to_right = left_index(right)
data = get_data(left_to_right)

print(data)
    
    
    