class SimpleHashSet:
    def __init__(self,size):
        self.size = size
        self.bucket = [[] for i in range(size)]
        
    def hashing(self,value):
        return sum(ord(i) for i in value) % self.size     
            
    def add(self,value):
        index = self.hashing(value)
        bucket = self.bucket[index]
        if value not in bucket: 
            bucket.append(value)
            
        
    def contains(self,value):
        index = self.hashing(value)
        bucket = self.bucket[index]
        return value in bucket

    def remove(self,value):
        index = self.hashing(value)
        bucket = self.bucket[index] 
        if value in bucket:
            bucket.remove(value)
            
    def print_set(self):
        print('Hashing table')
        for i,j in enumerate(self.bucket):
            print(i,j)      
                   
hash_set = SimpleHashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()                   


print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hashing('Adele'))