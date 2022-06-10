from sys import stdin

class Node:
    ch = None
    prev = None
    next = None
    
    def __init__(self, ch):
        self.ch = ch
        
def solution(s):
    result = ''
    head = Node('')
    tail = Node('')
    head.next = tail
    tail.prev = head
    cur = head
    
    for ch in s:
        if ch == '<':
            if cur != head:
                cur = cur.prev
        elif ch == '>':
            if cur.next != tail:
                cur = cur.next
        elif ch == '-':
            if cur != head:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = cur.prev
        else:
            new_node = Node(ch)
            new_node.prev = cur
            new_node.next = cur.next
            cur.next = new_node
            new_node.next.prev = new_node
            cur = new_node
    
    cur = head
    while cur.next != tail:
        cur = cur.next
        result += cur.ch
    
    return result

n = int(stdin.readline())
for _ in range(n):
    s = stdin.readline().rstrip()
    result = solution(s)
    print(result)