class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Empty Linked List')
            return 

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

if __name__=='__main__':
    l1=LinkedList()
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(20)
    l1.insert_at_beginning(10)
    l1.insert_at_end(110)
    l1.print()