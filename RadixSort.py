 
arr = [1,2,7,8,9,3,44,3,34,34,44,4,433,332,21,34]
m = max(arr)
c = [[],[],[],[],[],[],[],[],[],[]]
exp = 1

while m//exp > 0:
    while len(arr) > 0 :
        n = arr.pop()
        val = (n//exp) % 10
        c[val].append(n)
    for i in c:
        while len(i) > 0:
            va =i.pop()
            arr.append(va)    
        
  
    exp *= 10


print(arr)             
        
        
# a = [[],[],[],[],[]]   
# c=[[]]*10
# c[2].append(4)    
# print(c)