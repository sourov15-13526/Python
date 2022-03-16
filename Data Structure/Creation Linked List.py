# A simple Python program to introduce a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    # start with the empty list
    llist = LinkedList()

    llist.head = Node(5)
    second = Node(6)
    third = Node(7)

    llist.head.next = second
    second.next = third

    llist.printList()