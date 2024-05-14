class Node:
    def __init__(self, data):
        self.info = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None
    
    def Them(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def InNguocIterative(self):
        if self.head is None:
            return
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")

# Ví dụ sử dụng
dslk = DSLK()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print()
dslk.InNguocIterative()