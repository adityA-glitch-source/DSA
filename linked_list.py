class Node:
    def __init__(self,val):
        self.val = val
        self.next = next


Node1 = Node(4)
Node2 = Node(5)
Node3 = Node(6)
Node4 = Node(7)
Node5 = Node(8)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5



print(Node1.next.val)
print(Node1.val)
print(Node3)
print(Node4)
print(Node5)