class SimplehashMap:
    def __init__(self,size):
        self.size = size
        self.bucket = [[] for i in range(size)]
        
    def hashing(self,key):
        return sum(ord(i) for i in key) % self.size
    
    def put(self,key,value):
        index = self.hashing(key)
        bucket = self.bucket[index]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
        bucket.append((key,value))            
     
    def get (self,key):
        index = self.hashing(key)
        bucket = self.bucket[index]
        for i ,(k,v) in enumerate(bucket):
            if k == key:
                return v
        return None
    
    def remove(self,key):
        index = self.hashing(key)
        bucket = self.bucket
        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
       
    def print_map(self):
        for i,j in enumerate(self.bucket):
            print(i,j)   
            
     
hash_map = SimplehashMap(size=10)


hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()    


print(hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")

print("Name associated with '123-4570':", hash_map.get("123-4570"))
                