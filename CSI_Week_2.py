class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
    
    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        if n < 1:
            raise IndexError("Index must be 1-based (n >= 1)")
        
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(1, n - 1):
            if not current.next:
                raise IndexError("Index out of range")
            current = current.next
        
        if not current.next:
            raise IndexError("Index out of range")
        
        current.next = current.next.next

ll = LinkedList()

ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.add_node(50)

print("Original list:")
ll.print_list()

ll.delete_nth_node(3)
print("After deleting 3rd node:")
ll.print_list()

ll.delete_nth_node(1)
print("After deleting 1st node:")
ll.print_list()

ll.delete_nth_node(2)
print("After deleting 2nd node:")
ll.print_list()

print("Final list:")
ll.print_list()
