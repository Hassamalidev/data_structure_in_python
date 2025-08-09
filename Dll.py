from enum import nonmember


class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.length+=1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp=self.tail
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.tail=temp.prev
            self.tail.next=None
            temp.prev=None
            self.length-=1
        return temp
    def prepend(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        temp = self.head
        if self.head is None:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=temp.next
            temp.next=None
            self.head.prev=None
        self.length-=1
        return temp

    def get(self, index):
        if self.head is None:
            return None
        if index<self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp
        else:
            temp=self.tail
            for _ in range(self.length-1, index,-1):
                temp=temp.prev
            return temp
    def insert(self, index, value):
        if 0 > index >= self.length:
            return None
        before=self.get(index-1)
        after=before.next
        new_node = Node(value)
        if index==0:
           return  self.prepend(value)
        if index==self.length:
           return self.append(value)
        new_node.next=after
        after.prev=new_node
        before.next=new_node
        new_node.prev=before
        self.length+=1
        return new_node

    def set_value(self, index, value):
        if 0 > index >= self.length:
            return None
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def remove(self, index):
        if 0 > index >= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        before=temp.prev
        after=temp.next
        before.next=temp.next
        after=temp.prev
        temp.next= None
        temp.prev=None
        self.length-=1
        return temp

    def print_items(self):
        temp=self.head
        while temp is not None:
            print(temp.value, "<--->")
            temp=temp.next



dll=DoublyLinkedList(1)
dll.append(2)
dll.append(12)
dll.append(21)
dll.append(222)
dll.prepend(3)
print(dll.remove(3))
# dll.set_value(2,99)
# dll.insert(1, 234)
# print(dll.get(1).value)
# print(dll.pop_first())

# print(dll.pop())
# print(dll.pop())
# print(dll.pop())

dll.print_items()