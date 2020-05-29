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
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key) 
        
        node = self.storage[index]
        if node is None: #its open
            self.storage[index] = HashTableEntry(key, value)
            self.storage[index].next = node
        else:
            self.storage[index] = HashTableEntry(key, value)
                   

    def delete(self, key):
        if self.get(key) is not None: #item to del is found
            index = self.hash_index(key)
            node = self.storage[index]
            while node.next is not None:
                if node.key == key:
                    node.key = node.next.key
                    node.value = node.next.next
                    return
                else: # keep looking
                    node = node.next
            if node.key == key: #item is end of list
                node.key = None
                node.value = None
                node.next = None
        return None


    def get(self, key):
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None: #not empty
            while node.next is not None: #we have room to move right
                if node.key == key: #found it
                    return node.value
                else: #keep looking
                    node = node.next
            if node.key == key: # if head
                return node.value
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

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
