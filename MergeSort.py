# def mergeSort(arr):
#     if len(arr)  <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
    
#     sortsleft = mergeSort(left)
#     sortright = mergeSort(right)
    
#     return merge(sortsleft, sortright)
    
# def merge(left ,right):
#     result = []
#     i=j=0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result            

# arr=[1,2,3,4,45,56,5,6,67,7,7,8,8,97,54]
# s = mergeSort(arr)
# print(s)

# a = 10
# b = 5

# print(a+b)

a = 6
b = 9  
print(a+b)