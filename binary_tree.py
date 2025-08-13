class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node==temp:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            if new_node.value>temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contains(self, value):
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
               temp=temp.right
            else:
                return True
        return False


    def __r_contains(self, current_node , value):
        if current_node is None:
            return  False
        if value==current_node.value:
            return True
        if value<current_node.value:
            return self.__r_contains( current_node.left , value)
        if value>current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node , value):
        if current_node is None:
            return Node(value)
        if value<current_node.value:
            current_node.left=self.__r_insert(current_node.left, value)
        if value>current_node.value:
            current_node.right=self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
           self.root=Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node.value

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if value<current_node.value:
            current_node.left=self.__r_delete(current_node.left, value)
        elif value>current_node.value:
            current_node.right=self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node=current_node.right
            elif current_node.right is None:
                current_node=current_node.left
            else:
                sub_tree_min=self.min_value(current_node.right)
                current_node.value=sub_tree_min
                current_node.right=self.__r_delete(current_node.right, sub_tree_min)
        return current_node

    def r_delete(self, value):
        self.__r_delete(self.root, value)



tree=BinaryTree()
tree.r_insert(12)
tree.r_insert(121)
tree.r_insert(21)
tree.r_insert(10)
tree.r_insert(13)
tree.r_delete(12)
print(tree.r_contains(12))
# print(tree.min_value(tree.root))
# print(tree.contains(13))
print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)