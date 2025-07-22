class Hashmsp:
    def __init__(self):
        self.Max=100
        self.arr=[[] for i in range(self.Max)]

    def gen_map(self, key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.Max

    def __setitem__(self, key, value):
        h=self.gen_map(key)
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key, value))


    def __getitem__(self, key):
        h=self.gen_map(key)
        for element in  self.arr[h]:
            if element[0]==key:
               return element[1]


    def __delitem__(self, key):
        h=self.gen_map(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
              del self.arr[h][index]





t=Hashmsp()
t['march 6']=5
t['march 7']=4
t['march 8']=3
t['march 17']=6
t["apple 1"]=16
# del t['apple 1']
print(t.arr)
print(t["march 8"])
