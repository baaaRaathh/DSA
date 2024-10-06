# The linear Search Alogrithm search through an array and returm the index of the traget value 

def linearsearch(arr,tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return -1

arr = [1,2,3,4,5]
tar=7
result = linearsearch(arr,tar)
if result != -1:
    print(result)
else:
    print('Not fount')        



