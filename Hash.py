def Hashing(value):
    sum = 0
    for i in value:
        sum += ord(i)
    return sum % 10
v='Bob'
print(Hashing(v))       