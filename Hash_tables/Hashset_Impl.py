class hashset:
    def __init__(self,size):
        self.size=size
        self.buckets=[[] for i in range(size)]

    def add(self, value):
        index=self.hash_function(value)
        bucket=self.buckets[index]
        if value not in bucket:
            bucket.append(value)
    def remove(self,value):
        index=self.hash_function(value)
        bucket=self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def cotains(self,value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    def hash_function(self,value):
        return sum(ord(char) for char in value) % self.size
    def printset(self):
        print("Hash set")
        for index,value in enumerate(self.buckets):
            print("Index",index,'Value',value)
hash=hashset(20)
hash.add("A")
hash.add("B")
hash.add("C")
hash.add("D")
hash.printset()
hash.remove('A')
hash.printset()
print(hash.cotains('B'))