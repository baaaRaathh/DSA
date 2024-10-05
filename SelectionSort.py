
# a= [2,3,56,7,3,4,5,54,3,4,6,743,2,1]
# n = len(a)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if a[j] < a[min_index]:
#             min_index = j
#     min_value = a.pop(min_index)
#     a.insert(i,min_value)    
        
# print(a)        





a = [7,44,2,3,444,5,1,454,6,7]     #   [1, 7, 44, 2, 3, 444, 5, 454, 6, 7]
for i in range(len(a)-1):          #   [1, 2, 7, 44, 3, 444, 5, 454, 6, 7]
     m = i                         #   [1, 2, 3, 5, 7, 44, 444, 454, 6, 7]
    for j in range(i+1,len(a)):    #   [1, 2, 3, 5, 6, 7, 44, 444, 454, 7]
        if a[j] < a[m]:            #   [1, 2, 3, 5, 6, 7, 44, 444, 454, 7]
             m = j                 #   [1, 2, 3, 5, 6, 7, 7, 44, 444, 454]
    mv = a.pop(m)                   #  [1, 2, 3, 5, 6, 7, 7, 44, 444, 454]
     a.insert(i,mv)                 #  [1, 2, 3, 5, 6, 7, 7, 44, 444, 454]
print(a)        
    