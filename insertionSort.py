# for i in range(0,-1,-1):
#     print(i)

a = [23,45,53,1,2,4,4,5,55] 

# for i in range(1,len(a)):
#     insert_index = i
#     current_index = a.pop(i)
#     for j in range(i-1,-1,-1):
#         if a[j] > current_index:
#             insert_index = j
            
#     a.insert(insert_index,current_index) 
# print(a)                  
# [23, 45, 53, 1, 2, 4, 4, 5, 55]
# [23, 45, 53, 1, 2, 4, 4, 5, 55]
# [1, 23, 45, 53, 2, 4, 4, 5, 55]
# [1, 2, 23, 45, 53, 4, 4, 5, 55]
# [1, 2, 4, 23, 45, 53, 4, 5, 55]
# [1, 2, 4, 4, 23, 45, 53, 5, 55]
# [1, 2, 4, 4, 5, 23, 45, 53, 55]
# [1, 2, 4, 4, 5, 23, 45, 53, 55]            

for i in range(1,len(a)):
    index = i
    current = a.pop(i)
    for j in range(i-1,-1,-1):
        if a[j] > current:
            index = j
    a.insert(index,current)        
print(a)            
    
