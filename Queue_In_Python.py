class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self, value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def enqueue(self, value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            temp=self.last
            temp.next=new_node
            self.last=new_node
        self.length+=1
        return new_node
    def dequeue(self):
        if self.first is None:
            return None
        temp=self.first
        if self.length ==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp
    def is_empty(self):
        if self.first is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.first
    def size(self):
        return self.length

    def print_items(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next


queue=Queue(3)
queue.enqueue(2)
queue.enqueue(12)
queue.enqueue(22)
# print(queue.peek().value)

queue.print_items()
print("dequeue",queue.dequeue().value)
print("dequeue",queue.dequeue().value)
# print("dequeue",queue.dequeue().value)
# print("dequeue",queue.dequeue().value)
# print("dequeue",queue.dequeue())
print(queue.size())