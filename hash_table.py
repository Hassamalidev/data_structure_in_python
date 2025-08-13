class Hash_table:
    def __init__(self, size=7):
        self.data_map=[None]*size

    def _hash(self, key):
        my_hash=0
        for letter in key:
           my_hash= (my_hash+ord(letter)*7)%len(self.data_map)
        return my_hash
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(f"{i}:{val}")

    def set_item(self, key, value):
        index=self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index]=[]
        bucket = self.data_map[index]
        bucket.append([key, value])

    def get_item(self, key):
        index=self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index] [i] [0]==key:
                   return self.data_map[index] [i] [1]
        return None
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
               for j in range(len(self.data_map[i])):
                   all_keys.append(self.data_map[i][j][0])
        return all_keys


h=Hash_table()
h.set_item('washer', 200)
h.set_item('bolts', 100)
print(h.get_item("bolts"))
print(h.keys())
# h.print_table()
