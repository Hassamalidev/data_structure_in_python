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
        while temp is not None:
            print(f"{temp.value} --->")
            temp=temp.next




ll=LinkedList(11)
ll.append(12)
ll.prepend(13)
ll.append(23)
ll.reverse()
print(ll.get_by_value(12))
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
print(ll.print_items())