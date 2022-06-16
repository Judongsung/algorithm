from sys import stdin

class LinkedList:
    head = None
    tail = None
    cur = None
    
    def __init__(self, s):
        head = Node()
        tail = Node()
        head.right = tail
        tail.left = head
        self.cur = tail
        self.head = head
        self.tail = tail
        for ch in s:
            self.add(ch)
        return
    
    def move_left(self, ):
        if self.cur.left != self.head:
            self.cur = self.cur.left
        return
            
    def move_right(self, ):
        if self.cur.right != None:
            self.cur = self.cur.right
        return
    
    def add(self, ch):
        new_node = Node(ch)
        cur = self.cur
        new_node.left = cur.left
        new_node.right = cur
        new_node.left.right = new_node
        cur.left = new_node
        return
    
    def delete(self, ):
        cur = self.cur
        if cur.left == self.head:
            return
        cur.left.left.right = cur
        cur.left = cur.left.left
        return
    
    def get_all_data(self, ):
        result = []
        node = self.head
        while node.right != self.tail:
            node = node.right
            result += node.data
        return result
    
class Node:
    data = None
    left = None
    right = None
    
    def __init__(self, data=None):
        self.data = data
        
s = stdin.readline().rstrip()
ll = LinkedList(s)
m = int(stdin.readline())
for _ in range(m):
    query = stdin.readline().split()
    if query[0] == 'L':
        ll.move_left()
    elif query[0] == 'D':
        ll.move_right()
    elif query[0] == 'B':
        ll.delete()
    elif query[0] == 'P':
        ll.add(query[1])
result = ll.get_all_data()
print(''.join(result))