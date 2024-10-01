# n = [0]*10
# print(n)

def countSort(arr):
    m = max(arr)
    c = [0]*(m+1)
    
    while len(arr) > 0:
        n = arr.pop(0)
        c[n] += 1
      
    for i in range(len(c)):
        while c[i] > 0:
            arr.append(i)
            c[i] -= 1
    return arr   
arr = [1,23,3,3,4,5,5,3,2,4,5,6,7,8,6,67,5,4,4]
print(countSort(arr))               
        