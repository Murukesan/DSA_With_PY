class Hashmap:
    def __init__(self,size):
        self.size=size
        self.buckets=[[] for i in range(size)]
    def add(self,key,value):
        index=self.hash_function(key)
        bucket=self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))
    def hash_function(self,key):
        num_sum=sum(int(char) for char in key if char.isdigit())
        return num_sum%10
    def get(self,key):
        index=self.hash_function(key)
        bucket=self.buckets[index]
        for k,v in bucket:
            if k==key:
                return v
        return None
    def remove(self,key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return
    def Print(self):
        for i,v in enumerate(self.buckets):
            print('Index',i,'value',v)

hashmap=Hashmap(10)
hashmap.add("123-4567", "Charlotte")
hashmap.add("123-4568", "Thomas")
hashmap.add("123-4569", "Jens")
hashmap.Print()
print(hashmap.get('123-4567'))
hashmap.remove('123-4567')
hashmap.Print()
