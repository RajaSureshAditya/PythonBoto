class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedLists:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def delete_at_begining(self):
        itr = self.head
        node = Node(itr.next.data,itr.next.next)
        self.head = node

    def remove(self,data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def add_node(self,data):
        itr = self.head
        node = Node(data,itr)
        self.head = node

    def add_after_node(self, data,after):
        itr = self.head
        next_data = None
        while itr.next:
            if itr.data == after:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
    def reverselinkedlist(self):
        curr = self.head
        previous = None
        while curr:
            temp_curr = curr.next
            curr.next = previous
            previous = curr
            if not temp_curr:
                break
            curr = temp_curr
        self.head = curr

    def print(self):
        # print(self.head.data)
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        lststr = ""
        while itr:
            lststr += "--> "+str(itr.data)
            itr = itr.next
        print(lststr)
if __name__== '__main__':
    linkdlist = LinkedLists()
    linkdlist.insert_at_begining('Aditya')
    linkdlist.insert_at_begining('Raja')
    linkdlist.insert_at_begining('Suresh')
    linkdlist.insert_at_begining('Tinku')
    linkdlist.insert_at_begining('Bittu')
    linkdlist.insert_at_begining(24)
    linkdlist.print()
    # linkdlist.delete_at_begining()
    linkdlist.remove('Suresh')
    linkdlist.add_node('Bannu')
    linkdlist.add_after_node('Bablu','Tinku')
    linkdlist.print()
    linkdlist.reverselinkedlist()
    linkdlist.print()


