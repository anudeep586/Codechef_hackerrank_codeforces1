class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.next
        print(llstr)
    def print_backward(self):
        if self.head is None:
            raise Exception("Invalid operation you are performing")
        itr=self.head
        while itr.next:
            itr=itr.next
        llstr=''
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.prev
        print((llstr))


if __name__=='__main__':
    ll=doublelinkedlist()
    ll.insert_at_begining(45)
    ll.insert_at_begining(78)
    ll.insert_at_begining(86)
    ll.print_forward()
    ll.print_backward()
