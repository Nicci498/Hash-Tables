class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        fnvPrime = 2**40 + 2**8 + 0xb3 # 64 bit prime
        hash = 14695981039346656037 #offset basis
        for i in key:
            hash = hash * fnvPrime
            hash = hash ^ ord(i)
        return hash & 0xFFFFFFFFFFFFFFFF

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        hstEntry = HashTableEntry(key, value)
        node = self.storage[index]

        if node is not None:
            self.storage[index] = hstEntry
            self.storage[index].next = node
        else:
            self.storage[index] = hstEntry

    def delete(self, key):
        
        index = self.hash_index(key)
        node = self.storage[index]
        prev = None
        

        if node.key == key:
            self.storage[index] = node.next
            return 
        
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.storage[index].next = None
                return 
            
            prev = node
            node = node.next
        return

    def get(self, key):
        index = self.hash_index(key)
        node = self.storage[index]

        if node is not None: 
            while node: 
                if node.key == key: 
                    return node.value
                node = node.next
        return node

    def resize(self):
        self.storage = self.storage + [None] * self.capacity
        return self.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
