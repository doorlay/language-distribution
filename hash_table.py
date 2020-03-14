class HashTable:

    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None]*table_size
        self.num_items = 0 

    def insert(self, key):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

        hash_value = self.horner_hash(key)
        original_hash_value = hash_value
        i = 1
        while True:
            hash_value = hash_value % self.table_size
            if self.hash_table[hash_value] == None:
                self.hash_table[hash_value] = (key, 1)
                self.num_items += 1
                load_factor = self.get_load_factor()
                if load_factor > (1/2):
                    old_hash = self.hash_table
                    self.table_size = (self.table_size * 2) + 1
                    self.hash_table = [None] * self.table_size
                    for item in old_hash:
                        if item != None:
                            new_hash_value = self.horner_hash(item[0])
                            self.rehash(new_hash_value,item)
                break
            elif self.hash_table[hash_value][0] == key:
                new_value = self.hash_table[hash_value][1] + 1
                self.hash_table[hash_value] = (key, new_value)
                break
            elif i == self.table_size:
                break
            hash_value = original_hash_value + (i ** 2)
            i += 1  

    def rehash(self,hash_value,item):
        """ Function to rehash all items when the table size is increased, accounting for collisions."""

        original_hash_value = hash_value
        i = 1
        while True:
            hash_value = hash_value % self.table_size
            if self.hash_table[hash_value] == None:
                self.hash_table[hash_value] = item
                break
            elif self.hash_table[hash_value][0] == item[0]:
                new_value = self.hash_table[hash_value][1] + 1
                new_key = item[0]
                item = (new_key, new_value)
                self.hash_table[hash_value] = item
            elif i == self.table_size:
                break
            hash_value = original_hash_value + (i ** 2)
            i += 1
            
    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

        h = 0
        n = min(8, len(key))
        for i in range(n):
            h = (31*h)+ord(key[i])
        return h % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""

        hash_value = self.horner_hash(key)
        original_hash_value = hash_value
        i = 1
        while True:
            if hash_value > self.table_size - 1:
                hash_value = hash_value % self.table_size
            if self.hash_table[hash_value] == None:
                return False
            elif self.hash_table[hash_value][0] == key:
                return True
            elif i == self.table_size:
                return False
            hash_value = original_hash_value + (i ** 2)
            i += 1  

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""

        hash_value = self.horner_hash(key)
        original_hash_value = hash_value
        i = 1
        while True:
            if hash_value > self.table_size - 1:
                hash_value = hash_value % self.table_size
            if self.hash_table[hash_value] == None:
                return None
            elif self.hash_table[hash_value][0] == key:
                return hash_value
            elif i == self.table_size:
                return None
            hash_value = original_hash_value + (i ** 2)
            i += 1  

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""

        new_lst = []
        for item in self.hash_table:
            if item != None:
                new_lst.append(item[0])
        return new_lst

    def get_value(self, key):
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""

        hash_value = self.horner_hash(key)
        original_hash_value = hash_value
        i = 1
        while True:
            if hash_value > self.table_size - 1:
                hash_value = hash_value % self.table_size
            if self.hash_table[hash_value] == None:
                return None
            elif self.hash_table[hash_value][0] == key:
                return self.hash_table[hash_value][1]
            elif i == self.table_size:
                return None
            hash_value = original_hash_value + (i ** 2)
            i += 1  

    def get_num_items(self):
        """ Returns the number of entries (words) in the table. Must be O(1)."""

        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""

        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""

        return self.num_items / self.table_size