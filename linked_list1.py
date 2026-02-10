class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# Create the first Node(head of the list)
head = Node(5)

# Link the second Node
head.next = Node(10)

# Link the third Node
head.next.next = Node(15)

# Link the fourth Node
head.next.next.next = Node(20)

# printing linked list

temp = head
while temp is not None:
      print(temp.val ,  end = ' ')
      temp = temp.next