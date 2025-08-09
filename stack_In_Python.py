class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self, value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_items(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return  new_node

    def pop(self):
        if self.top is None:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height-=1
        return temp

    def is_empty(self):
        if self.top is None:
            return  True
        return False
    def peek(self):
        if self.is_empty():
            return None
        return self.top
    def size(self):
        return self.height

stack=Stack(5)
stack.push(6)
stack.push(15)
stack.push(454)
print(stack.peek().value)
print(stack.pop().value)
print(stack.is_empty())
print("size",stack.size())
stack.print_items()