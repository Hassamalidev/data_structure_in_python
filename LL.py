class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail = new_node
        if self.head is not None:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.head is None:
            return  None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value


    def prepend(self, value):
         new_node= Node(value)
         if self.head is None:
             self.head=new_node
             self.tail=new_node
         if self.head is not None:
            new_node.next=self.head
            self.head=new_node
         self.length+=1

    def pop_first(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        if self.length==0:
            self.tail = None
        self.length-=1
        return True

    def get_by_index(self, index):
        if 0 > index or index >= self.length:
            return  None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def get_by_value(self, value):
        temp=self.head
        while temp is not None:
            if temp.value==value:
                return temp
            temp = temp.next
        return None

    def get_index(self, value):
        if value not in self.print_items():
            return "Element not found in ll"
        else:
            temp=self.head
            index=0
            while temp.value != value:
                  temp=temp.next
                  index+=1
            return index

    def set_value(self, index, value):
        temp=self.get_by_index(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get_by_index(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    def insert_after_value(self, after_which, value):
        new_node=Node(value)
        if after_which  not in self.print_items():
            return "Element not found"
        else:
            temp=self.get_by_value(after_which)
            new_node.next=temp.next
            temp.next=new_node
            return new_node

    def remove(self, index):
        if 0 > index or index >=self.length:
            return  None
        if index==0:
            return self.pop()
        if index == self.length-1:
            return self.pop_first()
        prev=self.get_by_index(index-1)
        curr=prev.next
        prev.next=curr.next
        curr.next=None
        self.length-=1
        return curr
    def remove_by_value(self,value):
        index=self.get_index(value)
        if 0 > index or index >=self.length:
            return  None
        if index==0:
            return self.pop()
        if index == self.length-1:
            return self.pop_first()
        prev=self.get_by_index(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp


    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=self.head
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        return True

    def print_items(self):
        temp=self.head
        all_ll=[]
        while temp is not None:
            all_ll.append(temp.value)
            temp=temp.next
        return all_ll



ll=LinkedList(11)
ll.append(12)
ll.append(13)
ll.append(23)

# print(ll.get_by_value(12))
# print(ll.get(2))
# print(ll.pop_fir
# st())
# print(ll.pop_first())
# print(ll.pop_first())
# print(ll.pop_first())

# print(ll.pop())
# print(ll.pop())
# print(ll.pop())
# ll.set_value(1,22)
# ll.insert(1,31)
ll.insert_after_value(13,234)
ll.remove_by_value(12)
print(ll.print_items())
