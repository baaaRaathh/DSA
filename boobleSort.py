a=[1,2,3,4,5,5,5]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)    



a=[4,6,5,2,45,6]
t = 10

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        c=a[i:j]
        if t == sum(c):
            print(True)
            break
    if i == len(a)-1:
        print(False)