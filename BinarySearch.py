def binarysearch(arr,tar):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid =  (left+right)// 2
        
        if arr[mid] == tar:
            return mid
        
        if arr[mid] < tar:
            left = mid + 1
            
        else:
            right = mid -1    
            
    return -1        
            
arr = [1,2,3,4,5,6,7,8,9]
tar = 7

result = binarysearch(arr,tar)
if result != -1:
    print(result)
else:
    print('not fount')   
    
    
  