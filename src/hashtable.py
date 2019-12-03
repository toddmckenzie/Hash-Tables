
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):

        return hash(key)


    def _hash_djb2(self, key):
  
        pass


    def _hash_mod(self, key):
  
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key) #where to store value
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
            self.count += 1
            return self.storage[index].value
        elif self.storage[index] != None:
            lp = self.storage[index]
            while lp:
                if lp.key == key:
                    lp.value = value
                    return lp.value
                if not lp.next:
                    lp.next = LinkedPair(key, value)
                    return lp.next.value
                lp = lp.next

    def remove(self, key):
        index = self._hash_mod(key)
        if self.storage[index] != None:
            if self.storage[index].key == key:
                if self.storage[index].next == None:
                    self.storage[index] = None
                else:
                    self.storage[index] = self.storage[index].next
            elif self.storage[index] != None:
                lp = self.storage[index]
                while lp:
                    if lp.next:
                        if lp.next.key == key:
                            if lp.next.next:
                                lp.next = lp.next.next
                    lp = lp.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                lp = self.storage[index]
                while lp:
                    if lp.key == key:
                        return lp.value
                    lp = lp.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        tempStorage = self.storage
        self.capacity *= 2
        # for i in self.storage:
        #     tempStorage.append(i)

        self.storage = [None] * self.capacity
        for i in tempStorage:
            self.insert(tempStorage[i])


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")


# ht = HashTable(3)
# ht.insert('red', 'hello')
# ht.insert('blue', 'hi')
# ht.insert('green', 'yo')
# ht.insert('red1', 'hello')
# ht.insert('blue1', 'hi')
# ht.insert('green1', 'yo')
# ht.insert('red1', 'hello')
# ht.insert('blue2', 'hi')
# ht.insert('green2', 'yo')
# ht.insert('red2', 'hellosadfad')
# ht.insert('blue3', 'hi')
# ht.insert('green3', 'yo')
# print('*************')
# print('*************')
# print(ht.retrieve('red2'))
# print(ht.remove('red2'))
# print(ht.retrieve('red2'))
# print('*************')
# print('*************')
# ht.remove('green')
# print(ht.storage)
# print(ht.storage)
# ht.insert('blue', 'goodbye')
# ht.insert('hey', 'heyhey')
# ht.insert('what', 'whathwat')
# ht.remove('blue')
# print(ht.storage)
